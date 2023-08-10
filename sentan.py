import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


@st.cache
def load_data():
    data = pd.read_csv('./kartaslovsent.csv', sep=';', encoding='windows-1251')
    return data


st.header('Вывод данных')

input_google_autocomplete_keyword: str = st.text_input(
    "What is your seed keyword?")
data_load_state = st.text('Загрузка данных...')
data = load_data()
data_load_state.text('Данные загружены!')


if st.checkbox('Показать словарь'):
    st.subheader('Данные словаря')
    st.write(data)

with open('text.txt', 'w', encoding='utf-8') as f:
    f.write(input_google_autocomplete_keyword)

with open('text.txt', 'r', encoding='utf-8') as f:
    # читаем текст построчно
    total_value = 0
    count = 0
    for line in f:
        st.write(line)
        # разбиваем строку на слова
        words = line.split()

        # проходим по каждому слову
        for word in words:
            # проверяем, есть ли слово в датасете
            word = word.lower()
            #st.write(word)
            if word in data['term'].values:
                # если есть, то добавляем значение из поля value к общему значению

                total_value += data.loc[data['term'] == word, 'value'].values[0]
                count += 1
    if ( count != 0):
        res = total_value/count
        print(res)
        if (res > 0.5):
            st.write(res, 'Хороший отзыв')
        elif (res >= 0):
            st.write(res, 'Нейтральный отзыв')
        else:
            st.write(res, 'Плохой отзыв')
    else:
        st.write('Нейтральный отзыв')
    # выводим общее значение
