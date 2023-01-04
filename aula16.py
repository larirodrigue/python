import mysql.connector
import datetime

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="aula15",
)

cursor=connection.cursor()

sql='INSERT INTO matricula(RA,nome,nota,freq) VALUES(10, "Larissa", 10, 75)'
sql1='INSERT INTO matricula(RA,nome,nota,freq) VALUES(12, "Morgana", 7, 20)'
sql2='INSERT INTO matricula(RA,nome,nota,freq) VALUES(14, "Yasuo", 6, 30)'
sql3='INSERT INTO matricula(RA,nome,nota,freq) VALUES(16, "Yone", 8, 100)'
sql4='INSERT INTO matricula(RA,nome,nota,freq) VALUES(18, "Yuumi", 1, 90)'


cursor.execute(sql)
cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)

connection.commit()
cursor.close()
connection.close()

print('Foi cadastrado o novo usuário')
