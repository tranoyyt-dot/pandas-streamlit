import streamlit as st
from datetime import date, datetime

st.title("🎥 Sistema de Aluguel de Filmes - Drama / Suspense")

filmes = [
    "Duas Faces de um Crime (1996)",
    "Garota Exemplar (2014)",
    "Ilha do Medo (2010)",
    "Clube da Luta (1999)",
    "Os Suspeitos (2013)"
]

filme_escolhido = st.selectbox("🎞️ Selecione um filme para alugar:", filmes)

data_retirada = st.date_input("📅 Data de retirada:", min_value=date.today())
data_devolucao = st.date_input("📅 Data de devolução:", min_value=data_retirada)

if st.button("🎫 Registrar Aluguel"):
    st.subheader("📋 Informações do Aluguel")

    st.write(f"**Filme:** {filme_escolhido}")
    st.write(f"**Data de retirada:** {data_retirada.strftime('%d/%m/%Y')}")
    st.write(f"**Data de devolução:** {data_devolucao.strftime('%d/%m/%Y')}")

    hoje = date.today()
    dias_restantes = (data_devolucao - hoje).days

    st.markdown("### ⏳ Situação do Prazo:")
    if dias_restantes > 0:
        st.success(f"Faltam **{dias_restantes}** dia(s) para a devolução.")
    elif dias_restantes == 0:
        st.warning("⚠️ A devolução é **hoje**!")
    else:
        st.error(f"❌ O prazo já passou! Está com **{abs(dias_restantes)}** dia(s) de atraso.")
