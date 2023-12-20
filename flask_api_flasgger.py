#----------------------------------------------------------

#   Author: Shreyas Sanjay Korde ----------------------------
#   M. Sc. Mechatronics -------------------------------------
#   Project Name: Deployment of Bank Authentication web App -------------------

#----------------------------------------------------------


# to run the code after starting flask type "/apidocs" in webaddress like http://127.0.0.1:5000/apidocs

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger 
from flasgger import Swagger

app=Flask(__name__)     # from this point application will get started
Swagger(app)

pickle_in = open('classifier.pkl', 'rb')   # will open in read binary mode
classifier = pickle.load(pickle_in)

@app.route('/')   # decorator
def welcome():
    return 'welcome ALL'

@app.route('/predict')     #bydefault GET method
def predictiom_note_authentication():
    
    """Let's Start Authentication of bank notes
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
        
    responses:
        200: 
            description: The output values
    """
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    
  
    return str(prediction)

@app.route('/predict_file', methods=["POST"])
def predictiom_note_authentication_file():
    
    """Let's Start Authentication of bank notes using Test file
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200: 
            description: The output values for he file are
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    predictions=classifier.predict(df_test)
    
    return str(list(predictions))
    
    



# to run the code after starting flask type "/apidocs" in webaddress like http://127.0.0.1:5000/apidocs


if __name__=='__main__':
    app.run(debug=True)


# to run the code after starting flask type "/apidocs" in webaddress like http://127.0.0.1:5000/apidocs