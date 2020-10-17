# imports
import re
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import calendar

# def Get_date_in_pdf(sourceTxt):
#     date_format = [ r"\d{2} (?:%s) \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"\d{1} (?:%s) \d{4}" % '|'.join(calendar.month_abbr[1:]), r"\d{2} (?:%s) \d{4}" % '|'.join(calendar.month_name),  r"\d{1} (?:%s) \d{4}" % '|'.join(calendar.month_name[1:]), r"(?:%s) \d{2} \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"(?:%s) \d{1} \d{4}" % '|'.join(calendar.month_abbr[1:]), r"(?:%s) \d{2} \d{4}" % '|'.join(calendar.month_name),  r"(?:%s) \d{1} \d{4}" % '|'.join(calendar.month_name[1:]),r"\d{2} (?:%s), \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"\d{1} (?:%s), \d{4}" % '|'.join(calendar.month_abbr[1:]), r"\d{2} (?:%s), \d{4}" % '|'.join(calendar.month_name),  r"\d{1} (?:%s), \d{4}" % '|'.join(calendar.month_name[1:]), r"(?:%s) \d{2}, \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"(?:%s) \d{1}, \d{4}" % '|'.join(calendar.month_abbr[1:]), r"(?:%s) \d{2}, \d{4}" % '|'.join(calendar.month_name),  r"(?:%s) \d{1}, \d{4}" % '|'.join(calendar.month_name[1:])]

#     dats = []
#     f_dats = ''


#     for i in date_format:
#         if(re.findall(i, sourceTxt)):
#             dats.extend(re.findall(i, sourceTxt))
#         else:
#             ans = re.findall('([1-9]|1[0-9]|2[0-9]|3[0-1]|0[0-9])(.|-|\/)([1-9]|1[0-2]|2[0-9]|3[0-9])(.|-|\/)(20[0-9][0-9])',sourceTxt)
#             ans_f = [''.join(ans[i]) for i in range(len(ans))]
#             dats.extend(ans_f)
#     for sublist in dats:
#         if any(sublist): 
#             f_dats = sublist
#             break   
    
#     return f_dats


# Add your Computer Vision subscription key to your environment variables.
if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
else:
    print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()
# Add your Computer Vision endpoint to your environment variables.
if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
else:
    print("\nSet the COMPUTER_VISION_ENDPOINT environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()
# install --upgrade azure-cognitiveservices-vision-computervision by : pip install --upgrade azure-cognitiveservices-vision-computervision
# Authenticate client
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
# Analyze image

remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
# get image description
'''
Describe an Image - remote
This example describes the contents of an image with the confidence score.
'''
# print("===== Describe an image - remote =====")
# # Call API
# description_results = computervision_client.describe_image(remote_image_url )

# # Get the captions (descriptions) from the response, with confidence level
# print("Description of remote image: ")
# if (len(description_results.captions) == 0):
#     print("No description detected.")
# else:
#     for caption in description_results.captions:
#         print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))

# Get image category
'''
Categorize an Image - remote
This example extracts (general) categories from a remote image with a confidence score.
'''
# print("===== Categorize an image - remote =====")
# # Select the visual feature(s) you want.
# remote_image_features = ["categories"]
# # Call API with URL and features
# categorize_results_remote = computervision_client.analyze_image(remote_image_url , remote_image_features)

# # Print results with confidence score
# print("Categories from remote image: ")
# if (len(categorize_results_remote.categories) == 0):
#     print("No categories detected.")
# else:
#     for category in categorize_results_remote.categories:
#         print("'{}' with confidence {:.2f}%".format(category.name, category.score * 100))

# Read printed and handwritten text k



'''
Batch Read File, recognize handwritten text - remote
This example will extract handwritten text in an image, then print results, line by line.
This API call can also recognize handwriting (not shown).
'''
print("===== Batch Read File - remote =====")
# Get an image with handwritten text
# remote_image_handw_text_url = "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/master/articles/cognitive-services/Computer-vision/Images/readsample.jpg"
remote_image_handw_text_url = "https://slicedinvoices.com/pdf/wordpress-pdf-invoice-plugin-sample.pdf"

# Call API with URL and raw response (allows you to get the operation location)
recognize_handw_results = computervision_client.read(remote_image_handw_text_url,  raw=True)
# Get the operation location (URL with an ID at the end) from the response
operation_location_remote = recognize_handw_results.headers["Operation-Location"]
# Grab the ID from the URL
operation_id = operation_location_remote.split("/")[-1]

# Call the "GET" API and wait for it to retrieve the results 
while True:
    get_handw_text_results = computervision_client.get_read_result(operation_id)
    if get_handw_text_results.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

# Print the detected text, line by line
date_ans = ''
if get_handw_text_results.status == OperationStatusCodes.succeeded:
    for text_result in get_handw_text_results.analyze_result.read_results:
       
        for sourceTxt in text_result.lines:
            # print(line)
            # print(line.text)
            # print(line.bounding_box)
            def Get_date_in_pdf(sourceTxt):
                date_format = [ r"\d{2} (?:%s) \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"\d{1} (?:%s) \d{4}" % '|'.join(calendar.month_abbr[1:]), r"\d{2} (?:%s) \d{4}" % '|'.join(calendar.month_name),  r"\d{1} (?:%s) \d{4}" % '|'.join(calendar.month_name[1:]), r"(?:%s) \d{2} \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"(?:%s) \d{1} \d{4}" % '|'.join(calendar.month_abbr[1:]), r"(?:%s) \d{2} \d{4}" % '|'.join(calendar.month_name),  r"(?:%s) \d{1} \d{4}" % '|'.join(calendar.month_name[1:]),r"\d{2} (?:%s), \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"\d{1} (?:%s), \d{4}" % '|'.join(calendar.month_abbr[1:]), r"\d{2} (?:%s), \d{4}" % '|'.join(calendar.month_name),  r"\d{1} (?:%s), \d{4}" % '|'.join(calendar.month_name[1:]), r"(?:%s) \d{2}, \d{4}" % '|'.join(calendar.month_abbr[1:]),  r"(?:%s) \d{1}, \d{4}" % '|'.join(calendar.month_abbr[1:]), r"(?:%s) \d{2}, \d{4}" % '|'.join(calendar.month_name),  r"(?:%s) \d{1}, \d{4}" % '|'.join(calendar.month_name[1:])]

                dats = []
                f_dats = ''


                for i in date_format:
                    if(re.findall(i, sourceTxt)):
                        dats.extend(re.findall(i, sourceTxt))
                    else:
                        ans = re.findall('([1-9]|1[0-9]|2[0-9]|3[0-1]|0[0-9])(.|-|\/)([1-9]|1[0-2]|2[0-9]|3[0-9])(.|-|\/)(20[0-9][0-9])',sourceTxt)
                        ans_f = [''.join(ans[i]) for i in range(len(ans))]
                        dats.extend(ans_f)
                for sublist in dats:

                    if any(sublist): 
                        f_dats = sublist
                        break   
                return f_dats
            abc = Get_date_in_pdf(sourceTxt.text)
            if(abc == ''):
                continue
            else:
                date_ans = abc
                break
            
    print(date_ans)

print("Apiyo")

