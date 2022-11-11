from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import matplotlib.pyplot as plt

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = "c3f83fd12eef463cb0432303eca09f21"
endpoint = "https://comparadorimagenesia.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''

'''
Quickstart variables
These variables are shared by several examples
'''
# Images used for the examples: Describe an image, Categorize an image, Tag an image, 
# Detect faces, Detect adult or racy content, Detect the color scheme, 
# Detect domain-specific content, Detect image types, Detect objects
images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
remote_image_url = "https://github.com/TristanDom/AUSB-AI/blob/main/PaginasEscaneadas/PaginasConfiables/adobe.png"
'''
END - Quickstart variables
'''


'''
Tag an Image - remote
This example returns a tag (key word) for each thing in the image.
'''
print("===== Tag an image - remote =====")
# Call API with remote image
tags_result_remote = computervision_client.tag_image(remote_image_url )

# Print results with confidence score
print("Tags in the remote image: ")
if (len(tags_result_remote.tags) == 0):
    print("No tags detected.")
else:
    for tag in tags_result_remote.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
print()
'''
END - Tag an Image - remote
'''
print("End of Computer Vision quickstart.")


print("===== Analyze an image - remote =====")
# Select the visual feature(s) you want.

remote_image_features = ["tags"]

# Call API with URL and features
results_remote = computervision_client.analyze_image(remote_image_url , remote_image_features, remote_image_details)

# Print results with confidence score
print("Categories from remote image: ")
if (len(results_remote.categories) == 0):
    print("No categories detected.")
else:
    for category in results_remote.categories:
        print("'{}' with confidence {:.2f}%".format(category.name, category.score * 100))
print()


# Return tags
# Print results with confidence score
print("Tags in the remote image: ")
if (len(results_remote.tags) == 0):
    print("No tags detected.")
else:
    for tag in results_remote.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))

# Detect landmarks
print("Landmarks in the remote image:")
if len(results_remote.categories.detail.landmarks) == 0:
    print("No landmarks detected.")
else:
    for landmark in results_remote.categories.detail.landmarks:
        print(landmark["name"])