import mysql.connector
import datetime

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="aula15")
cursor = conexao.cursor()
#delete
comando = f'DELETE FROM matricula WHERE ra=18'
cursor.execute(comando)

conexao.commit() #edita o banco de dados