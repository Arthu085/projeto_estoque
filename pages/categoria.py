import streamlit as st
from uteis import categoria_def as cd

st.title("Adicionar Categorias")
categoria_nome = st.text_input("Digite o nome da Categoria:", placeholder="Digite o nome da nova categoria")
categoria_desc = st.text_input("Digite a descrição da Categoria:", placeholder="Digite o nome da nova descrição da categoria")

if st.button("Adicionar Categoria"):
    if categoria_nome and categoria_desc:
        cd.add_categoria(categoria_nome, categoria_desc)
        st.success("Categoria Adicionada com Sucesso!")
    else:
        st.error("Por favor, preencha todos os campos.")        

