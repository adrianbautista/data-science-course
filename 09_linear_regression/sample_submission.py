"""
Casual Model: Thee following features have the highest signifiance in predicting number of guest riders per day.
They make sense because A, B, and C.

Registered Model: Likewise the registered model shared some significance in features,
though the p-values changed for one particular feature. I think this is because D.

"""
import sklearn.linear_model as lm
import pandas as pd

days = pd.read_csv('data/day.csv')

## This section is clearly underdeveloped, but consider how to take advantage of the print outs from statsmodels,
##  or dig around to find your assorted metric needs in the sklearn modules: metrics, feature_selection
g_model, r_model = lm.LinearRegression(), lm.LinearRegression()

g_model.fit(days[['holiday', 'atemp', 'hum']], days['casual'])

print g_model.score(days[['holiday', 'atemp', 'hum']], days['casual'])

r_model.fit(days[['holiday', 'atemp', 'hum']], days['registered'])

print r_model.score(days[['holiday', 'atemp', 'hum']], days['registered'])

