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
--Visualizar los salarios mayores para cada oficio.
select max(SALARIO) as SALARIOSMAYORES, OFICIO
from EMP
group by OFICIO;
--Buscar aquellos departamentos con cuatro o 
--más personas trabajando.
select count(*) as PERSONAS, DEPT_NO
from EMP
group by DEPT_NO
having count(*) >= 4;
--Visualizar el número de enfermeros, enfermeras e interinos que 
--hay en la plantilla, ordenados por la función.
select count(*) as PERSONAS, FUNCION
from PLANTILLA
where FUNCION IN ('INTERINO', 'ENFERMERO', 'ENFERMERA')
group by FUNCION;
--Visualizar departamentos, oficios y número de personas, 
--para aquellos departamentos 
--que tengan dos o más personas trabajando en el mismo oficio.
select count(*) as PERSONAS, OFICIO, DEPT_NO
from EMP
group by OFICIO, DEPT_NO
having count(*) >= 2; 
--Calcular el salario medio de la plantilla de la sala 6, 
--según la función que realizan. 
--Indicar la función y el número de empleados.
select avg(SALARIO) AS MEDIASALARIAL, FUNCION
, count(*) as EMPLEADOS
from PLANTILLA
where SALA_COD = 6
group by FUNCION;
--Averiguar los últimos empleados que se 
--dieron de alta en la empresa en cada uno de los oficios
--, ordenados por la fecha.
select max(FECHA_ALT) as MAXFECHAALTA, OFICIO
from EMP
group by OFICIO
order by MAXFECHAALTA desc;
--Mostrar el número de enfermeras que existan por cada sala.
select count(*) AS ENFERMERAS, SALA_COD
from PLANTILLA
where FUNCION = 'ENFERMERA'
group by SALA_COD;














