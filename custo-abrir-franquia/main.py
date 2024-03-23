import csv
import chardet

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import streamlit as st

st.title("Previsão Inicial de Custo para Franquia")

@st.cache_data
def load_data(archive):
    encoding = detect_encoding(archive)
    delimiter = detect_delimiter(filename=archive, encoding=encoding)
    return pd.read_csv(archive, sep=delimiter, encoding=encoding)

def detect_delimiter(filename: str, encoding: str) -> str:
    with open(filename, 'r', encoding=encoding) as file:
        sample = file.read(1024)
    sniffer = csv.Sniffer()
    return sniffer.sniff(sample).delimiter

def detect_encoding(filename: str) -> str:
    with open(filename, 'rb') as file:
        raw_data = file.read(1024)
    result = chardet.detect(raw_data)
    return result['encoding']

dados = load_data(archive="data/slr12.csv")

X = dados[['FrqAnual']]
y = dados['CusInic']

modelo = LinearRegression().fit(X,y)

col1, col2 = st.columns(2)

with col1:
    st.header("Dados")
    st.table(dados.head(10))

with col2:
    st.header("Gráfico de Dispersão")
    fig, ax = plt.subplots()
    ax.scatter(X,y, color='blue')
    ax.plot(X, modelo.predict(X), color='red')
    st.pyplot(fig)

st.header("Valor Anual da Franquia:")
novo_valor = st.number_input("Insira Novo Valor",min_value=1.0, max_value=999999.0,value=1500.0, step=0.01)
processar = st.button("Processar")

if processar:
    dados_novo_valor = pd.DataFrame([[novo_valor]], columns=['FrqAnual'])
    prev = modelo.predict(dados_novo_valor)
    st.header(f"Previsão de Custo Inicial R$: {prev[0]:.2f}")
