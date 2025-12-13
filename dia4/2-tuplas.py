dias = ('lunes', 'martes', 'miercoles', 'jueves', 'viernes')
#las tuplas son inmutables, no se pueden modificar despues de cr
#la diferencia con la listas es que estas son con parentesis redondos y las listas con corchetes
print(f'tipo de dato original:{type(dias)}')
dias=list(dias)
print(f'tipo de dato modificado:{type(dias)}')
dias.append('sabado')
dias=tuple(dias)

print(dias)


#aqui el profesor explico sobre las tuplas y su inmutabilidadrearla
#no se pueden agregar ni eliminar elementos de una tupla

#cambio de ser tupla a lista 

#'usualmente no se cambia una tupla a lista, pero en casos especiales se puede hacer'

#una tupla se usa cuando extraes una carpeta / informacion externa y deseas trabajar con ella para que no sea modificada los datos 

