#----------------------------------------------------------

#   Author: Shreyas Sanjay Korde ----------------------------
#   M. Sc. Mechatronics -------------------------------------
#   Project Name: Deployment of Bank Authentication web App -------------------

#----------------------------------------------------------

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle


app=Flask(__name__)     # from this point application will get started
pickle_in = open('classifier.pkl', 'rb')   # will open in read binary mode
classifier = pickle.load(pickle_in)

@app.route('/')   # decorator
def welcome():
    return 'welcome ALL'

@app.route('/predict')     #bydefault GET method
def predictiom_note_authentication():
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return 'The predicted value is ' + str(prediction)

@app.route('/predict_file', methods=["POST"])
def predictiom_note_authentication_file():
    df_test=pd.read_csv(request.files.get("file"))
    predictions=classifier.predict(df_test)
    
    return 'The predicted values are ' + str(list(predictions))
    
    






if __name__=='__main__':
    app.run(debug=True)
