"""

from Scrap import scrapper


scrapper(query = "bouteille", mode = "*")

"""



'''
import requests
image = open("camera/100-gobelets-transparent.jpg", 'rb').read()
endpoint = ("https://triofcv.cognitiveservices.azure.com/customvision/v3.0/Prediction/72e7b78b-9edd-4dd2-a90d-7870228699f3/classify/iterations/Iteration2/image")
headers = { "Prediction-Key" : "3584e049dbb44462a1ccda0647352be8" , "Content-Type" : "application/octet-stream" }

request = requests.post(endpoint, headers = headers, data = image)

request.raise_for_status()

pred = request.json()

resultat = []
for element in pred['predictions'] :
    resultat.append( ("{objet} à {chance} % " .format (objet = element['tagName'], chance = round(element['probability']) * 100 )) )

print(resultat)
'''

import glob
import os
path = "camera/"

list_of_files = glob.glob(path+'/*')
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)