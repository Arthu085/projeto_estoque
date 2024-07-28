import connection_sql as cs
import mysql.connector

def add_categoria(categoria_nome, categoria_descc):
    connection = cs.get_db_connection()
    cursor = connection.cursos()
    query = "INSERT INTO categoria (nome, descc) VALUES (%s)"
    cursor.execute(query, (categoria_nome, categoria_descc))
    connection.commit()
    cursor.close()
    connection.close()
