import streamlit as st
import lda

data_exists = False
data_is_correct = True

with st.sidebar:
	st.header('header')
	data_file = st.file_uploader('choose file')

	if data_file is not None:
		st.button('retrain the model')

if data_exists and data_is_correct:
	st.write('nice and good data')

	st.button('train the model')
	st.button('predict')
else:
	st.write('bad or no data')

st.write(lda.AdvancedLDA())
