from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import (
    TextOperationStatusCodes,
    ComputerVisionErrorException
)
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv

import os
import sys
import time
import click

# load the environment
load_dotenv()


@click.group()
def cli():
    pass


@cli.command("file")
@click.argument('filename', type=click.Path(exists=True))
def perform_ocr_of_local_file(filename):
    client = create_computer_vision_client()
    ocr_result = ocr_file(client, filename)
    lines = extract_text_from_ocr_result(client, ocr_result)
    for line in lines:
        print(line)


@cli.command("url")
@click.argument('url')
def perform_ocr_of_remote_file(url):
    client = create_computer_vision_client()
    ocr_result = ocr_url(client, url)
    lines = extract_text_from_ocr_result(client, ocr_result)
    for line in lines:
        print(line)


def create_computer_vision_client():
    '''
    Creates the ComputerVisionClient instance
    '''

    if "COMPUTER_VISION_SUBSCRIPTION_KEY" in os.environ:
        subscription_key = os.environ["COMPUTER_VISION_SUBSCRIPTION_KEY"]
    else:
        print("Set the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.")
        print("**Restart your shell or IDE for changes to take effect.**")
        sys.exit(1)

    if "COMPUTER_VISION_ENDPOINT" in os.environ:
        endpoint = os.environ["COMPUTER_VISION_ENDPOINT"]
    else:
        print("Set the COMPUTER_VISION_ENDPOINT environment variable.")
        print("**Restart your shell or IDE for changes to take effect.**")
        sys.exit(1)

    # create the ComputerVisionClient
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key)
)
    return computervision_client


def ocr_file(client, filepath):
    '''
    Calls Azure Computer Vision API to read a file stream
    Returns the result object
    '''

    with open(filepath, "rb") as image_stream:
        recognize_printed_results = client.batch_read_file_in_stream(
            image_stream, raw=True
        )

        return recognize_printed_results


def ocr_url(client, image_url):
    '''
    Calls Azure Computer Vision API to read the contents of a file via a public url
    Returns the result object
    '''

    recognize_printed_results = client.batch_read_file(image_url,  raw=True)
    return recognize_printed_results


def extract_text_from_ocr_result(client, ocr_result):
    '''
    Takes the result object of a Computer Vision batch read operation
    and extracts the text
    '''

    # the result object contains a call-back URL
    operation_location_remote = ocr_result.headers["Operation-Location"]

    # Grab the ID from the URL
    operation_id = operation_location_remote.split("/")[-1]

    # Poll the call-back URL until we get a status that is not "Running" or "NotStarted"
    while True:
        get_printed_text_results = client.get_read_operation_result(
            operation_id
        )
        if get_printed_text_results.status not in ["NotStarted", "Running"]:
            break
        time.sleep(0.5)

    # Print the detected text, line by line
    if get_printed_text_results.status == TextOperationStatusCodes.succeeded:
        for text_result in get_printed_text_results.recognition_results:
            for line in text_result.lines:
                yield line.text

    else:
        print("OCR call failed")
        sys.exit(1)


if __name__ == "__main__":
    cli()
