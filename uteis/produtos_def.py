import connection_sql as cs
import mysql.connector

def encontrar_categoria():
    connection = cs.get_db_connection()
    cursor = connection.cursor()
    query = "SELECT nome FROM categoria ORDER BY nome"
    connection.commit()
    cursor.close()
    connection.close()

def add_produto(nome_produto, categoria_nome):
    connection = cs.get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO produto (nome, categoria_id) VALUES (%s, %s)"    
    connection.commit()
    cursor.close()
    connection.close()