import pandas as pd
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import LeaveOneOut
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

df = pd.read_csv('sepsis_data.csv')
#add sorting genes alphabetically and target at last
print('db size: ',df.shape)

def Evaluate():
	X = df[['PLAC8', 'CEACAM4', 'LAMP1', 'PLA2G7']]#rewrite this to any given genes, sorted
	y = df['Target']
	
	y_true = []
	y_pred = []
	
	#cross-validation should usually be k-fold but since we have a poor samplesize using Leave-One-Out for now
	for train_idx, test_idx in LeaveOneOut().split(X):
		X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
		y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
		
		#scaler only trains on train!
		scaler = StandardScaler()
		X_train_scaled = scaler.fit_transform(X_train)
		X_test_scaled = scaler.transform(X_test)
		
		lda = LinearDiscriminantAnalysis()
		lda.fit(X_train_scaled, y_train)
		
		#predicting our test unit
		pred = lda.predict(X_test_scaled)[0]
		
		y_pred.append(pred)
		y_true.append(y_test.iloc[0])
	
	return classification_report(y_true, y_pred, target_names=['Сепсис', 'Не сепсис'])


def Predict():
	pass
