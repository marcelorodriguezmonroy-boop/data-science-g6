# DICCIONARIOS
# Son colecciones desordenadas de elementos que se almacenan en pares clave-valor. 
# Cada clave es única y se utiliza para acceder a su valor correspondiente.
# Se definen utilizando llaves {} y los pares clave-valor se separan por comas.
#parecido al formato jayson
capitales = {
    "Perú":"Lima",
    "Ecuador":"Quito",
    "Colombia":"Bogota",
    "Argentina":"Buenos Aires"
}

# acceder al valor de una clave
print(capitales["Ecuador"]) # Output: Quito

#agregar o modificar un par clave-valor
capitales["Chile"] = "Santiago" #agregar
capitales["Perú"] = "Lima Metropolitana" #modificar

print(capitales)




# Eliminar un par clave-valor
del capitales['Argentina']
capital_eliminada = capitales.pop('Ecuador','NO EXISTE')
print(F'Se elimino la capital{capital_eliminada}')
print(capitales)


#recorrer un diccionario

for clave in capitales.keys():
    print(clave)

# por valor 
for valor in capitales.values():
    print(valor)

# por clave valor 
for clave, valor in capitales.items():
    print(f'La capital de {clave} es {valor}')  
        
