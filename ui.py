import streamlit as st
import qda
#import storage_handler
import os
import sys
import streamlit as st

# Определяем, запущена ли программа как .exe или как обычный скрипт
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Универсальный путь к твоей базе данных
CSV_PATH = os.path.join(BASE_DIR, "sepsis_data.csv")

#st.write('st.session_state:', st.session_state)#debug

if st.toggle('Показать текущий отчёт модели'):
    st.code(qda.Evaluate())

st.markdown('#')

st.markdown('Ввод данных тестируемого пациента:')
tested_patient = {'PLAC8':232707.0, 'CEACAM4':2780.0, 'LAMP1':159.0, 'PLA2G7':0, 'BETA':2519837.0}

for key in tested_patient:
    tested_patient[key] = st.number_input(f'{key}:',step=1)


if st.button('Спрогнозировать'):
    prediction = qda.Predict(tested_patient)
    if prediction == 1:
        st.write('Прогноз: **Сепсис**')
    else:
        st.write('Прогноз: **Не сепсис**')