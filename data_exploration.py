# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 11:32:56 2021

https://www.kaggle.com/dansbecker/basic-data-exploration

@author: maths
"""

import pandas as pd
mel_file_path = 'D:/python/melb_data.csv'
melbourne_data = pd.read_csv(mel_file_path)

k = melbourne_data.describe()

print(k)


