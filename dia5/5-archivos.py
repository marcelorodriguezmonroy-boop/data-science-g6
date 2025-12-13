with open('alumnos .txt', 'w') as archivo:
  archivo.write('Marcelo Rodriguez')
  archivo.write('\n)')
  archivo.write('carlos perez')
  
with open('alumnos .txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)    