import pickle
import os
import pandas as pd

DB_PATH = 'sepsis_data.csv'

df = pd.read_csv(DB_PATH)
df_new = pd.read_csv('new_data.csv')

def update_data():#df_new into arguments
	df_updated = pd.concat([df,df_new],ignore_index=True)
	df_updated.drop_duplicates(inplace = True)
	df_updated.to_csv(index = True)

def load_data():
	return df
