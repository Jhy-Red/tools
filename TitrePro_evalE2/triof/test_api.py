#!/usr/bin/python3



# Configuration
ENDPOINT = "https://triofcv.cognitiveservices.azure.com/customvision/v3.0/Prediction/6b09ae54-19f6-4fa8-b0b7-40a1be376684/classify/iterations/Standart/image"
prediction_key = "45a365eacbd74858ab02810d7a72c89c"
prediction_ressource_id = "/subscriptions/50f55159-0c1b-4154-9452-e079e6b5e663/resourceGroups/LK_triof/providers/Microsoft.CognitiveServices/accounts/triofcv"

# Itteration 1
project_id = "6b09ae54-19f6-4fa8-b0b7-40a1be376684"
publish_iteration_name = "Standart"


def checking_img(ENDPOINT
                , prediction_key
                , prediction_ressource_id
                , project_id
                , publish_iteration_name):
    
    # Import list #
    from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
    from msrest.authentication import ApiKeyCredentials

    base_image_location = "camera/"
    #image_contents = open(base_image_location + "GOBELETS-PLASTIQUES-118AB.jpg", "rb").read()
    image_contents = open("camera/520003_1.jpg", "rb").read()


    #from PIL import Image
    #return Image.open("camera/520003_1.jpg").show()

    # USE IA #
    prediction_credentials = ApiKeyCredentials( in_headers={ 
                                                            "Content-Type" : "application/octect-stream" 
                                                            , "Prediction-Key": prediction_key
                                                            }
                                                #,in_query= {
                                                #            "Body" : image_contents
                                                #            }
                                                            )
    
    predictor = CustomVisionPredictionClient(api_key = prediction_credentials,endpoint= ENDPOINT)
    
    results = predictor.classify_image(project_id, publish_iteration_name, image_contents)

        

    # Display the results / STORE IT TO RESTAURE IT IN HTML.
    display_list_result = []
    for prediction in results.predictions:
        display_list_result.append(prediction.tag_name +": {0:.2f}%".format(prediction.probability * 100))
    
    return display_list_result
    



checking_img(ENDPOINT,prediction_key,prediction_ressource_id,project_id,publish_iteration_name)