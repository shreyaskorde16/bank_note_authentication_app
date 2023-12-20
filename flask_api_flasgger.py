#----------------------------------------------------------

#   Author: Shreyas Sanjay Korde ----------------------------
#   M. Sc. Mechatronics -------------------------------------
#   Project Name: Deployment of Bank Authentication web App -------------------

#----------------------------------------------------------

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

@app.route('/predict', method=['GET'])     #bydefault GET method
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
    
  
    return 'The predicted value is ' + str(prediction)

@app.route('/predict_file', methods=["POST"])
def predictiom_note_authentication_file():
    df_test=pd.read_csv(request.files.get("file"))
    predictions=classifier.predict(df_test)
    
    return 'The predicted values are ' + str(list(predictions))
    
    






if __name__=='__main__':
    app.run(debug=True)
