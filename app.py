# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:25:53 2022

@author: riskf
"""
from flask import Flask, request
from flask import jsonify, render_template
import pickle
import numpy as np
import os

#pathFile='C:\\Users\\riskf\\OneDrive\\Documents\\Courses\\AEC Spécialiste en intelligence artificielle\\Courses\\7 - 420-A57-BB - Mise en place d’un écosystème d’IA\\TP\\NLP_Classification\\'
pathFile="/user/src/app/"
#os.chdir(pathFile)

app = Flask(__name__, template_folder=pathFile)
#app = Flask(__name__)

model_pickle = pickle.load(open('voting.pkl', 'rb'))
selector=pickle.load(open('vector.pkl','rb'))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():

    final_features = request.form['message']
    final_features = selector.transform([final_features]).toarray()
    prediction = model_pickle.predict(final_features)
    output = prediction[0]
    

    return render_template('home.html', prediction_text='Le texte est associé à : {}'.format(output))

@app.route('/api',methods=['POST'])
def results():

    #data = request.get_json(force=True)
    final_features = request.get_json()['message']
    final_features = selector.transform([final_features]).toarray()
    prediction = model_pickle.predict(final_features)
    #prediction = model_pickle.predict(data)

    output = prediction[0]
    return jsonify(output)

#if __name__ == "__main__":
#    app.run(debug=True)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=80, debug=False)