import pandas as pd
import streamlit as st

st.title("Analisador de Filmes")

uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dados Originais")
    st.dataframe(df)

    st.subheader("Estatísticas")
    st.write(df.describe())

    df['Idade_do_Filme'] = 2025 - df['Ano']
    st.write(df)

    st.subheader("Gráfico de Avaliação")
    st.bar_chart(df.set_index('Título')['Avaliação'])
