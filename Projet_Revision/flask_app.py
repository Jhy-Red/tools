from flask import Flask           # app de base
from flask import render_template # template HTML

app = Flask(__name__, 
            template_folder='templates', 
            static_folder= 'static',
            )

@app.route('/') #page d'accueil
def welcome():
    msg = "Bienvenu sur le site de révision de la formation Simplon IA 2019"
    return render_template('accueil.html', message = msg)

@app.route('/Arbres_de_decision/') #page d'accueil
def decision_three():
    msg = "Arbres de décisions (CART pour Classification And Regression Trees)"
    return render_template('decision_tree.html', message = msg)

@app.route('/Nettoyage/') #page d'accueil
def cleaning_data():
    msg = "Nettoyage de donées"
    return render_template('cleaning_data.html', message = msg)















# Region de lancement
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug = True)