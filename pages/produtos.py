import streamlit as st
from uteis import produtos_def as pd

st.title("Adicionar Produtos")
produto_nome = st.text_input("Digite o nome do Produto:", placeholder="Digite o nome do novo produto")
categorias = pd.encontrar_categoria()
produto_categoria = st.selectbox("Selecione a Categoria:", options=categorias)


if st.button("Adicionar Produto"):
    if produto_nome and produto_categoria:
        pd.add_produto(produto_nome, produto_categoria)
        st.success("Produto Adicionado com Sucesso!")
    else:
        st.error("Por favor, preencha todos os campos.")   