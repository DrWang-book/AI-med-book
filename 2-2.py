import pandas as pd
df = pd.read_csv('data/diabetes_binary_5050split_health_indicators_BRFSS2015.csv')
selected_columns = ['HighBP', 'HighChol', 'BMI', 'GenHlth', 'DiffWalk','Age']

from sklearn.model_selection import train_test_split
data = df[selected_columns]
targets = df[['Diabetes_binary']]
X_train, X_test, y_train, y_test = train_test_split(data, targets, test_size=0.20, random_state=10)
y_train = y_train.values.ravel()
y_test = y_test.values.ravel()

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
print("reg.coef_:  ", reg.coef_.tolist())
print("intercept_:  ", reg.intercept_)

print("X_test:  \n", X_test[:3])
print("y_test:  \n", y_test[:3])
result=reg.predict(X_test).tolist()
print(result[:3])

y_test=y_test.tolist()
ct=0
for i in range(len(result)):
    if (result[i]>0.5 and y_test[i]==1) or (result[i]<=0.5 and y_test[i]==0):
        ct+=1
print(ct, len(result), ct/len(result))

