import streamlit as st
import qda
#import storage_handler
#import os
#import sys
import streamlit as st

col1, col2, col3 = st.columns(3,
                              vertical_alignment='center')
with col1:
    data_file = st.file_uploader('Выберите файл',
                                 help='Target - первый столбец, 1 - Сепсис, 0 - Не сепсис',
                                 type = ['csv'],)
    if data_file is not None:
        qda.ReInitData(data_file)
with col2:
    pass

with col3:
    if st.button('Использовать пробную выборку',
                 use_container_width = True,):
        qda.InitDefaults()
        data_file = None
        st.rerun()

if data_file and qda.df is None:
    st.error("Не выбран файл с данными")
else:
    classification_report = qda.Evaluate()
    
    with st.container(border=True):
        st.markdown('Ввод данных тестируемого пациента:')
        sample = qda.Sample()
        tested_patient = st.data_editor(
                sample, 
                num_rows = 'fixed',
                use_container_width = True,
                hide_index = True,)
    
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


            col1,col2 = st.columns(2,
                                   vertical_alignment = 'center')
            with col1:
                st.download_button(
                    label = 'Экспорт таблицы',
                    data = edited_df.to_csv(),
                    file_name='saved_data.csv',
                    use_container_width=True,)
            with col2:
                if st.button('Сохранить как по-умолчанию',
                             use_container_width=True,):
                    try:
                        edited_df.to_csv("data.csv", index=False)
                        st.success('База данных успешно обновлена')    
                        st.rerun()
                    except Exception as e:
                        st.error(f'Не удалось сохранить файл. Ошибка: {e}')
                
    if st.toggle('Показать отчёт модели'):
        st.code(classification_report)
