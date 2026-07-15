import streamlit as st
import qda
#import storage_handler
#import os
#import sys
import streamlit as st

CSV_PATH = 'data.csv'
data_file = st.file_uploader("Выберите файл", type = ["csv"])

if data_file is None:
    st.error("Не выбран файл с данными")
else:
    qda.ReInitData(data_file)
    classification_report = qda.Evaluate()
    
    with st.container(border=True):
        st.markdown('Ввод данных тестируемого пациента:')
        sample = qda.Sample()
        tested_patient = st.data_editor(
                sample, 
                num_rows = 'fixed',
                use_container_width = True,)
    
        if st.button('Спрогнозировать'):
            tp_vector = tested_patient.to_numpy()
            prediction = qda.Predict(tp_vector)
            if prediction == 1:
                st.write('Прогноз: **Сепсис**')
            else:
                st.write('Прогноз: **Не сепсис**')
    
    if st.toggle('Редактор данных'):
        with st.container(border=True):
            
            edited_df = st.data_editor(qda.df,num_rows='dynamic',key='data')
            if st.button('Сохранить'):
                try:
                    edited_df.to_csv("data.csv", index=False)
                    st.success("База данных успешно обновлена")    
                    st.rerun()
                except Exception as e:
                    st.error(f"Не удалось сохранить файл. Ошибка: {e}")
    
    if st.toggle('Показать отчёт модели'):
        st.code(classification_report)
