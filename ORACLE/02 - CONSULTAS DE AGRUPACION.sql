--Mostrar el número de empleados de la tabla
select count(*) as REGISTROS from EMP;
--Podemos combinar varias funciones en una misma consulta
--Mostrar número de empleados y la suma salarial de todos
select count(*) as REGISTROS
, sum(SALARIO) as SUMASALARIAL from EMP;
--Queremos saber el número de empleados por cada oficio.
select count(*) as EMPLEADOS, OFICIO from EMP
group by OFICIO;
--Mostrar el máximo salario, número de personas
--por cada oficio y por cada departamento.
select max(SALARIO) as MAXIMOSALARIO
, count(*) as PERSONAS, OFICIO, DEPT_NO
from EMP
group by OFICIO, DEPT_NO;
--Mostrar el número de personas por cada OFICIO
--pero solamente mostrando DIRECTOR Y ANALISTA
select count(*) as PERSONAS, OFICIO
from EMP
where OFICIO in ('ANALISTA', 'DIRECTOR')
group by OFICIO;
--Mostrar el número de empleados por cada oficio
--pero solamente mostrando los oficios dónde tengamos 
--más de 2 personas trabajando.
select count(*) as PERSONAS, OFICIO
from EMP
group by OFICIO
having count(*) > 2;
--Mostrar la suma salarial por cada oficio
--solamente de las personas que tengan una comisión 
--mayor a cero y cuya suma salarial sea mayor a 515000
select sum(SALARIO) as SUMASALARIAL, OFICIO
from EMP
where COMISION > 0
group by OFICIO
having sum(SALARIO) > 515000;
















