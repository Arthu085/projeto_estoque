import streamlit as st
from uteis import categoria_def as cd

st.title("Adicionar Categoria")
st.text_input("Digite o nome da Categoria:", placeholder="Digite o nome da nova categoria")
st.text_input("Digite a descrição da Categoria:", placeholder="Digite o nome da nova descrição categoria")


