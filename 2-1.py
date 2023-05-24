import pandas as pd
df = pd.read_csv('diabetes_binary_5050split_health_indicators_BRFSS2015.csv')
print(df.columns)
print(df.head())
print(round(df.corr(method='pearson'),2)['Diabetes_binary'])