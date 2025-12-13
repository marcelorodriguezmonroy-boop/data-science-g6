## Listas 
dias=['lunes','martes','miercoles','jueves','viernes']

#estoy creando una variable llamada dias que contiene una lista de los dias de la semana 
#voy a imprimir la lista completa 'print(dias)'
#recuperar info de la lista

print(dias[0])
#parecido aa la formula array, coomienza en 0 la coordenada o sea lunes es 0, martes es 1, miercoles es 2 etc



#agregar elementos a lista 
dias.append('sabado')

#append es un metodo que sirve para agregar elementos a la lista

#eliminar elementos de la lista
dias.pop(2)
del dias[0:2]

#recorrer la lista con un ciclo for
for dia in dias:
#for es un contador que va a ir recorriendo la lista
#recorrer todos los dias de la lista e imprimirlos uno por uno
    print(dia)