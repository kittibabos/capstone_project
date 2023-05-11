#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:44:33 2023

@author: kittibabos
"""

import json
import requests

url = 'http://127.0.0.1:8000/churn_prediction_regression'

input_data_for_model = {
    
    'equip_Yes' : 0,
    'internet_Yes' : 0,
    'ebill_Yes' : 0,
    'equipmon' : 0.0,
    'callcard_No' : 0,
    'cardten' : 110.0,
    'callcard_Yes' : 1,
    'age' : 44,
    'ebill_No' : 1,
    'internet_No' : 1,
    'longmon' : 3.70,
    'employ' : 5,
    'longten' : 37.45,
    'equip_No' : 0,
    'loglong' : 1.308,
    'tenure' : 13
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data = input_json)

print(response.text)