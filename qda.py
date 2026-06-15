import pandas as pd
import numpy as np

from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.model_selection import LeaveOneOut
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report


CSV_PATH = 'data.csv'
df = pd.read_csv(CSV_PATH)
#print('db size: ',df.shape)

X = df[['PLAC8', 'CEACAM4', 'LAMP1', 'PLA2G7', 'BETA']]#rewrite this to any given genes, sorted
y = df['Target']

scaler = StandardScaler()
a = QuadraticDiscriminantAnalysis() 


def Evaluate():
	y_true = []
	y_pred = []
	#cross-validation should usually be k-fold but since we have a poor samplesize using Leave-One-Out for now
	for train_idx, test_idx in LeaveOneOut().split(X):
		X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
		y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
		

		#scaler only trains on train!
		X_train_scaled = scaler.fit_transform(X_train)
		X_test_scaled = scaler.transform(X_test)
		
		#print('X_test: ', X_test, '\nX_test_scaled: ', X_test_scaled)
		
		a.fit(X_train_scaled, y_train)
		#predicting our test unit
		pred = a.predict(X_test_scaled)[0]
		
		y_pred.append(pred)
		y_true.append(y_test.iloc[0])
	
	return classification_report(y_true, y_pred, target_names=['Сепсис', 'Не сепсис'])


def Predict(tested_patient):
	X_tested = pd.DataFrame(tested_patient, index = [0])
	X_train_scaled = scaler.fit_transform(X)
	test_scaled = scaler.transform(X_tested)
	pred = a.predict(test_scaled)[0]
#	prob = a.predict_proba(test_scaled)[0]
	return pred

#print(Evaluate())
