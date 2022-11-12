from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

# Replace with valid values
ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"
training_key = "c3f83fd12eef463cb0432303eca09f21"
prediction_key = "69ca85c4f62940439a0e71c084ada721"
prediction_resource_id = "/subscriptions/b4dbd004-9e91-48d4-9bbe-e70896ded8f6/resourceGroups/AUSB-AI/providers/Microsoft.CognitiveServices/accounts/AUSB-IA"
publish_iteration_name = "ModeloFinal"
project_id = "efd48c83-3ed8-4dde-a275-234866477704"

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)



credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)


# Now there is a trained endpoint that can be used to make a prediction
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

with open(os.path.join ("/home/hunter/Documentos/AUSB-AI/PaginasEscaneadas/", "test.png"), "rb") as image_contents:
    results = predictor.classify_image(
        project_id, publish_iteration_name, image_contents.read())

    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))