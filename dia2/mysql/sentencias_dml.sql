-- SENTENCIAS DML
-- CRUD
-- C - INSERT
-- R - SELECT
-- U - UPDATE
-- D - DELETE

--INSERT
insert into alumnos(nro_documento,nombre) values('100','cesar mayta');
-- INSERTAR VARIOS REGISTROS
insert into alumnos(nro_documento,nombre)
VALUES
('200','Ana Martinez'),
('300','Luis Lopez'),
('400','Arturo Gonzales'),
('500','Monica Tejada'),
('600','Raul Rivera'),
('700','Andrea Valencia'),
('800','Sofia Mamani'),
('900','Carlos Perez'),
('1000','Jesus Concha');

-- ACTUALIZAR DATOS(UPDATE)

update alumnos SET
email = 'codigo@gmail.com';
-- UPDATE CON WHERE
update alumnos 
set email='cesar@gmail.com' where id = 1;
-- UPDATE CON FUNCIONES
update alumnos
set email = CONCAT(lower(replace(nombre,' ' ,'.')),'@gmail.com') where id > 1;


-- SELECT
select * from alumnos;
select nombre,email from alumnos;
select nombre from alumnos where id > 5;
select * from alumnos order by nombre asc;

-- DELETE
delete from alumnos where id = 3;
truncate table alumnos;
#manipulo datos, como insertar, hacer CRUD como menciona arriba
#truncar te limpia todo vs delete from - borra completamente (queda como residuos en el motor de la base de datos - continua el correlativo)
#cuando usas trunca elimina todos los redisuos, por eso que el correlativo se reinicia

#ya no se usa delete > colocan una columna mas con "activo" y "inactivo", y despues no lo insertas o filtras solo con los activos, 
#imagina que un trabajador vuelva a ala empresa, lo activas de nuevo 