import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="aula",
)

cursor = connection.cursor()

sql='INSERT INTO matricula(RA,nome,nota,freq) VALUES(10, "Larissa", 10, 75)'

cursor.execute(sql)

connection.commit()
cursor.close()
connection.close()

print('Foi cadastrado o novo usuário')
