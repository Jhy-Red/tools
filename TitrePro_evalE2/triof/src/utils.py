import os
import random
from matplotlib.image import imread

    
def checking_img(ENDPOINT
                , prediction_key
                , prediction_ressource_id
                , project_id
                , publish_iteration_name):
    
    # Import list #
    from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
    from msrest.authentication import ApiKeyCredentials

    # USE IA #
    prediction_credentials = ApiKeyCredentials(in_headers={ "Content-Type" : "application/octect-stream", 
                                                            "Prediction-key": prediction_key})
    
    predictor = CustomVisionPredictionClient(api_key = prediction_credentials,endpoint= ENDPOINT)
    base_image_location = "PromoIA/En cours/TitrePro_evalE2/triof/camera/"
     
    with open(base_image_location + "GOBELETS-PLASTIQUES-118AB.jpg", "rb") as image_contents:
        results = predictor.classify_image(project_id, publish_iteration_name, image_contents.read())

        

    # Display the results / STORE IT TO RESTAURE IT IN HTML.
    display_list_result = []
    for prediction in results.predictions:
        display_list_result.append(prediction.tag_name +": {0:.2f}%".format(prediction.probability * 100))
    
    return display_list_result
    
def open_waste_slot():

    """
        open the machine so that
        an user can enter the machine

    :return:
    """

    send_command_to_machine("open_waste_slot")
    return True


def close_waste_slot():
    """
    close the waste box for user safety
    :return:
    """

    send_command_to_machine("close_waste_slot")
    return True


def process_waste(waste_type):

    """
    move the good slot and shredd the waste
    :return:
    """

    move_container(waste_type)
    was_sucessful = shred_waste()

    return was_sucessful


def move_container(waste_type):

    BOTTLE_BOX = 0
    GLASS_BOX = 1
    command_name = "move_container"

    if waste_type == "bottle":
        send_command_to_machine(command_name, BOTTLE_BOX)
    elif waste_type == "glass":
        send_command_to_machine(command_name, GLASS_BOX)

    return True


def send_command_to_machine(command_name, value=None):

    """
    simulate command sending to rasberry pi
    do nothing to work even if the machine is not connected

    :param command_name:
    :param value:
    :return:
    """
    return True



def shred_waste():

    send_command_to_machine("shred_waste")

    return True


def take_trash_picture():

    """
        function simulating the picture taking
        inside the machine. 

        Call this function to ask the machine to 
        take picture of the trash

        return : np array of the picture
    """

    send_command_to_machine("take_picture")

    paths = os.listdir('camera')
    path = random.choice(paths)

    return imread(os.path.join("./camera", path))
