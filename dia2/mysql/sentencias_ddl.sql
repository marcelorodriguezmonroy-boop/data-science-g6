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