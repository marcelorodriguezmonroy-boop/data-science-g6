import mysql.connector

#creo conexión a mi bd
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='db_g6_'
)

print(f'estas conectado a la base de datos {connection.database}')

# alumno_cursor = connection.cursor()
# alumno_cursor.execute("insert into alumno (nro_documento, nombre) values ('1002', 'Jesus Lopez')")
# connection.commit()
# print("Alumno insertado correctamente")
# connection.close()

alumno_cursor_select = connection.cursor()
alumno_cursor_select.execute("select nro_documento, nombre from alumno")
resultado = alumno_cursor_select.fetchall()
for registro in resultado:
    print ('*'*20)
    print(f'Nro Documento: {registro[0]}')
    print (f'Nombre: {registro[1]}')

connection.close()
