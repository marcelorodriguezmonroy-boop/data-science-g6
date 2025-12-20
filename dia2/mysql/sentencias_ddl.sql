#en formato DDL 
#SENTENCIAS DDL 
# CREATE TABLE 
CREATE TABLE alumnos(
    ID INT not NULL PRIMARY KEY AUTO_INCREMENT,
    nro_documento VARCHAR(20) not NULL,
    nombre VARCHAR(255) not NULL,
    email VARCHAR(100)
)

# ALTER TABLE
ALTER TABLE alumnos
add nota int DEFAULT 0;

#eliminar table 
drop table alumnos

CREATE TABLE empresa(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    ruc VARCHAR(12) NOT NULL UNIQUE,
    razon_social VARCHAR(255) NOT NULL, 
    direccion TEXT
);  
#creo tablas y elimino
#varchar es hasta 255 caracteres, text es infinito
#not null es para que no haya invalidos 

#para el bootcamo es suficiente esto 