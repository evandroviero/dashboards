import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date

st.header("Meu Titulo")
st.markdown('# Meu texto')
st.caption('Balloons. Hundreds of them...')
st.write("# Ola", ['Item 0', 'Item 1'])

df = pd.DataFrame(
     np.random.randn(10, 3),
     columns=['Preço', 'Taxa de desocupação', 'Taxa inadiplencia',])

st.table(df)
st.line_chart(df)
st.bar_chart(df)

if st.button('MEU BOTÃO'):
     st.write('Click')

opcoes = ['Opção 1', 'Opção 2']
check = st.checkbox("Selecione as opções desejadas", opcoes)

if check:
     st.write('Marcado')

option = st.selectbox(
    'Selecione',
    ('Op 1', 'Op 2', 'Op 3'))

st.write('Você selecionou:', option)

options = st.multiselect(
     'Cor favorita',
     ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
     ['Vermelho', 'Verde'])

for i in range(5):
    st.columns(5)
    num = st.checkbox(f'{i}')
    if num:
        st.markdown(f'this is {i}')


values = st.slider('Intervalo',0.0, 100.0, (25.0, 75.0))
nome = st.text_input('Nome')
senha = st.text_input('Senha', type='password')
number = st.number_input('Número', min_value=0.0)
d = st.date_input("Digite uma data", datetime.now(), format="DD/MM/YYYY")