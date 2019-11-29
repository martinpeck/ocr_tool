from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import (
    TextOperationStatusCodes,
)
from msrest.authentication import CognitiveServicesCredentials

import os
import sys
import time

# load any .env file that might exist
from dotenv import load_dotenv
load_dotenv()

# Add your Computer Vision subscription key to your environment variables.
if "COMPUTER_VISION_SUBSCRIPTION_KEY" in os.environ:
    subscription_key = os.environ["COMPUTER_VISION_SUBSCRIPTION_KEY"]
else:
    print("Set the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.")
    print("**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

# Add your Computer Vision endpoint to your environment variables.
if "COMPUTER_VISION_ENDPOINT" in os.environ:
    endpoint = os.environ["COMPUTER_VISION_ENDPOINT"]
else:
    print("Set the COMPUTER_VISION_ENDPOINT environment variable.")
    print("**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

computervision_client = ComputerVisionClient(
    endpoint, CognitiveServicesCredentials(subscription_key)
)


print("===== Batch Read File In Stream =====")

remote_image_to_ocr = ""
# remote_image_to_ocr = "https://sample.com/page1.jpg"
local_image_to_ocr = "images/page1.jpg"

if remote_image_to_ocr:
    # Call API with URL and raw response (allows you to get the operation location)
    recognize_printed_results = computervision_client.batch_read_file(
        remote_image_to_ocr,  raw=True
    )

elif local_image_to_ocr:
    with open("images/page1.jpg", "rb") as image_stream:
        # Call API with file stream and raw response (allows you to get the operation location)
        recognize_printed_results = computervision_client.batch_read_file_in_stream(
            image_stream, raw=True
        )

else:
    print("No file specified.")
    sys.exit()

# Get the operation location (URL with an ID at the end) from the response
operation_location_remote = recognize_printed_results.headers["Operation-Location"]
# Grab the ID from the URL
operation_id = operation_location_remote.split("/")[-1]

# Call the "GET" API and wait for it to retrieve the results
while True:
    get_printed_text_results = computervision_client.get_read_operation_result(
        operation_id
    )
    if get_printed_text_results.status not in ["NotStarted", "Running"]:
        break
    time.sleep(1)

# Print the detected text, line by line
if get_printed_text_results.status == TextOperationStatusCodes.succeeded:
    for text_result in get_printed_text_results.recognition_results:
        for line in text_result.lines:
            print(line.text)
print()
