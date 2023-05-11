#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 19:31:16 2023

@author: kittibabos
"""

import pandas as pd
from pydantic import BaseModel
import json
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from fastapi import FastAPI

app = FastAPI()

class model_input(BaseModel):
    
    
    df : str
    scaler : str
    test_size : float
    random_state : int
    
    
@app.post('/churn_prediction_regression')

def data_prep(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    df = input_dictionary['df']
    scaler = input_dictionary['scaler']
    test_size = input_dictionary['test_size']
    random_state = input_dictionary['random_state']
    
    y = df['churn'].values
    X = df.drop(columns = ['churn'])

    features = X.columns.values
    scaler.fit(X)
    X = pd.DataFrame(scaler.transform(X))
    X.columns = features
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size, random_state)
    model_regression = LogisticRegression()
    model_regression.fit(X_train, y_train)
    prediction_test = model_regression.predict(X_test)
    accuracy_score = metrics.accuracy_score(y_test, prediction_test)
    return accuracy_score