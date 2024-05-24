# -*- coding: utf-8 -*-
"""Expriement.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IHdX0RYN2McpkjgapVXO5U8LxLFLa47F
"""

import os

import pandas as pd

wines = pd.read_csv("winequality-red.csv")
wines.head()



from sklearn.model_selection import train_test_split


X = wines.drop(['quality'], axis=1)
y = wines['quality']




X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)


from sklearn.linear_model import ElasticNet

lr = ElasticNet(alpha=0.1, l1_ratio=0.5, random_state=42)
lr.fit(X_train, y_train)

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)

    return rmse, mae, r2

predicted_value = lr.predict(X_test)


(rmse, mae, r2) = eval_metrics(y_test, predicted_value)

print("rmse = ", rmse)
print("mae = ", mae)
print("r2 = ", r2)

