import mysql.connector

#creo conexión a mi bd
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='db_g6_'
)

print(f'estas conectado a la base de datos {connection.database}')

