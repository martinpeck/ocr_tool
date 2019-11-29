# OCR Tool

A Python script that uses Azure Congitize Services to OCR text from images.

## Usage

This tool allows two types of operation; you can either ask it to stream a local image to the Azure services,
or you can pass the URL to a publicly accessible image.

If you run the script without any parameters you will see the following help text:

``` bash
$ python main.py --help     
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  file  Sends a local file to OCR to extract text
  url   Sends a file, accessible via a public url, to OCR to extract text
```

### Extracting Text from a Local Image File

The `file` command will allow you to extract text from a local image file.

The help text for this command:

``` bash
$ python main.py file --help
Usage: main.py file [OPTIONS]

  Sends a local file to OCR to extract text

Options:
  --filepath PATH  Submits a local file to OCR  [required]
  --help       Show this message and exit.
```

For example:

``` bash
$ python main.py file --filepath images/example1.jpg
```

### Extracting Text from an Image File via Publicly Addressable URL

The `url` command will allow you to extract text from an image file at the end of a publicly addressable url.

The help text for this command:

``` bash
$ python main.py url --help
Usage: main.py url [OPTIONS]

  Sends a file, accessible via a public url, to OCR to extract text

Options:
  --url TEXT  Submits a public url to OCR  [required]
  --help      Show this message and exit.
```

For example:

``` bash
python main.py url --url https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/printed_text.jpg
```

## Setup

### Create an Azure Cognitive Services Account

To use this script you will need to create an Azure Cognitive Services account.

<https://azure.microsoft.com/en-gb/free/services/cognitive-services/>

Once set up, you will need to grab the following two pieces of information:

1. Your Computer Vision Subscription Key
2. You Computer Vision endpoint URL

### Create Environment Variables

Two environment variables are required. You can either set these up as environment variables before running the tool, or you can create a `.env` file and the code will load this file when executed.

The file `.env-example` is a template file. Copy or rename this file to `.env`, and then replace the `{{REPLACE_ME}}` text with the appropriate values.

The environment variables values that are required are as follows"

| Name | Description |
|---|---|
|`COMPUTER_VISION_SUBSCRIPTION_KEY` | A token that identifies your Computer Vision subscription key. You get this value from the Azure Portal when you set up an Azure Cognitive Services account |
|`COMPUTER_VISION_ENDPOINT`| A URL to an endpoint. You get this value from the Azure Portal when you set up an Azure Cognitive Services account |

## References

### Python SDK, Cognitive Services, Computer Vision: Read printed and handwritten text

<https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts-sdk/python-sdk#read-printed-and-handwritten-text>

### batch_read_file

<https://docs.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-computervision/azure.cognitiveservices.vision.computervision.operations.computervisionclientoperationsmixin?view=azure-python#batch-read-file-url--custom-headers-none--raw-false----operation-config->

### batch_read_file_in_stream

<https://docs.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-computervision/azure.cognitiveservices.vision.computervision.operations.computervisionclientoperationsmixin?view=azure-python#batch-read-file-in-stream-image--custom-headers-none--raw-false--callback-none----operation-config->