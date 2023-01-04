import mysql.connector
import datetime

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="aula15")
cursor = conexao.cursor()
#update
comando = f'UPDATE matricula SET freq = "{20}",freq = "{75}" WHERE ra = 12'
print(comando)
cursor.execute(comando)

conexao.commit() #edita o banco de dados