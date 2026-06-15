import streamlit as st
import qda
#import storage_handler
#import os
#import sys
import streamlit as st

with st.container(border=True):
    st.markdown('Ввод данных тестируемого пациента:')
    tested_patient = {'PLAC8':0, 'CEACAM4':0, 'LAMP1':0, 'PLA2G7':0, 'BETA':0}

    for key in tested_patient:
        tested_patient[key] = st.number_input(f'{key}:',step=1,key=f'{key}')

    if st.button('Спрогнозировать'):
        prediction = qda.Predict(tested_patient)
        if prediction == 1:
            st.write('Прогноз: **Сепсис**')
        else:
            st.write('Прогноз: **Не сепсис**')

if st.toggle('Редактор данных'):
    with st.container(border=True):
        
        edited_df = st.data_editor(qda.df,num_rows='dynamic',key='data')
        if st.button('Сохранить'):
            try:
                edited_df.to_csv(qda.CSV_PATH, index=False)
                st.success("База данных успешно обновлена")    
                st.rerun()
            except Exception as e:
                st.error(f"Не удалось сохранить файл. Ошибка: {e}")

if st.toggle('Показать текущий отчёт модели'):
    st.code(qda.Evaluate())