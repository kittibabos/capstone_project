# -*- coding: utf-8 -*-
"""
Spyder Editor - kitti

"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    
    equip_Yes : int
    internet_Yes : int
    ebill_Yes : int
    equipmon : float
    callcard_No : int
    cardten : float
    callcard_Yes : int
    age : int
    ebill_No : int
    internet_No : int
    longmon : float
    employ : int
    longten : float
    equip_No : int
    loglong : float
    tenure : int
    
# loading the saved model

churn_model_regression = pickle.load(open('churn_model_regression.sav' , 'rb'))

@app.post('/churn_prediction_regression')

def churn_pred_regression(input_parameters : model_input):

    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    equip_Yes = input_dictionary['equip_Yes']
    internet_Yes = input_dictionary['internet_Yes']
    ebill_Yes = input_dictionary['ebill_Yes']
    equipmon = input_dictionary['equipmon']
    callcard_No = input_dictionary['callcard_No']
    cardten = input_dictionary['cardten']
    callcard_Yes = input_dictionary['callcard_Yes']
    age = input_dictionary['age']
    ebill_No = input_dictionary['ebill_No']
    internet_No = input_dictionary['internet_No']
    longmon = input_dictionary['longmon']
    employ = input_dictionary['employ']
    longten = input_dictionary['longten']
    equip_No = input_dictionary['equip_No']
    loglong = input_dictionary['loglong']
    tenure = input_dictionary['tenure']
    
    input_list = [equip_Yes, internet_Yes, ebill_Yes, equipmon, callcard_No, cardten, callcard_Yes, age, ebill_No, internet_No, longmon, employ, longten, equip_No, loglong, tenure]
    
    prediction = churn_model_regression.predict([input_list])
    
    if prediction[0] == 0:
        return 'Customer will not churn'
    else:
        return 'Customer is likely to churn'
    
    
    
    
    
    
    