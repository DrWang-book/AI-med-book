import pandas as pd
df = pd.read_csv('data/heart.csv')
print(df.info())
print(df.head())

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder() 
df['Sex']=le.fit_transform(df['Sex'])
df['ChestPainType']=le.fit_transform(df['ChestPainType'])
df['RestingECG']=le.fit_transform(df['RestingECG'])
df['ExerciseAngina']=le.fit_transform(df['ExerciseAngina'])
df['ST_Slope']=le.fit_transform(df['ST_Slope'])
print(df.head())

from sklearn.model_selection import train_test_split
data = df.drop(columns='HeartDisease')
targets=df[['HeartDisease']]
X_train, X_test, y_train, y_test = train_test_split(data, targets, test_size=0.20, random_state=10)

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth=3)
clf.fit(X_train,y_train)
print(clf.feature_importances_)

from sklearn.metrics import classification_report, confusion_matrix
pred = clf.predict(X_test)
clf_report = classification_report(y_test, pred)
print(clf_report)
print(confusion_matrix(y_test, pred))