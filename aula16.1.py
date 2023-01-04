import mysql.connector
import datetime

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="aula")
cursor = conexao.cursor()
#READ
comando = f'SELECT ra, nome, nota, freq FROM matricula'
cursor.execute(comando)
r = cursor.fetchall() #ler banco de dados
print(r)

for i in r:
    if i[2] >= 5 and i[3] >=75:
        print("Aprovado", i[1])
    else:
        print('Reprovado', i[1])