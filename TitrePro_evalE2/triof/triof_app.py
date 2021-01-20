from flask import Flask, render_template, request, url_for
from src.utils import *

app = Flask(__name__,static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/start')
def insert():

    open_waste_slot()

    return render_template('insert.html')

@app.route('/start_auto_detect')
def insert_correct():
    import glob
    import os
    path = "static/camera/"
    
    list_of_files = glob.glob(path+'/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    
    import requests
    image = open(latest_file, 'rb').read()
    endpoint = ("https://triofcv.cognitiveservices.azure.com/customvision/v3.0/Prediction/72e7b78b-9edd-4dd2-a90d-7870228699f3/classify/iterations/Iteration2/image")
    headers = { "Prediction-Key" : "3584e049dbb44462a1ccda0647352be8" , "Content-Type" : "application/octet-stream" }

    request = requests.post(endpoint, headers = headers, data = image)

    #request.raise_for_status()

    pred = request.json()

    result = []
    for element in pred['predictions'] :
         result.append("{objet} à {chance} % " .format (objet = element['tagName'], chance = round(element['probability'],2) * 100 ))
        
    
    return render_template('insert correct.html', prediction = result , img = latest_file)


@app.route('/waste/pick-type')
def pick_type():
    close_waste_slot()

    return render_template('type.html')
    

@app.route('/confirmation', methods=['POST'])
def confirmation():
    waste_type = request.form['type']

    process_waste(waste_type)
    return render_template('confirmation.html')



if __name__ == "__main__":
    app.run(debug=True)
    