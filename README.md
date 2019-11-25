# OCR Tool

A basic Python script that uses Azure Congitize Services to OCR text from images.

## Setup

### Create an Azure Cognitive Services Account

To use this script you will need to create an Azure Cognitive Services account.

<https://azure.microsoft.com/en-gb/free/services/cognitive-services/>

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