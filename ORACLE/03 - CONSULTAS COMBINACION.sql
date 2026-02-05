select TABLA1.CAMPO1, TABLA1.CAMPO2
, TABLA2.CAMPO1, TABLA2.CAMPO2
from  TABLA1 
inner join TABLA2
on TABLA1.CAMPORELACION = TABLA2.CAMPORELACION;
--Mostrar el Apellido, Oficio, Nombre de departamento, Localidad
--de los empleados.
select EMP.APELLIDO, EMP.OFICIO
, DEPT.DNOMBRE, DEPT.LOC
from EMP
inner join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO;
--Mostrar el Apellido, Oficio, Nombre departamento y Localidad
--de los empleados de SEVILLA
select EMP.APELLIDO, EMP.OFICIO
, DEPT.DNOMBRE, DEPT.LOC
from EMP
inner join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO
where DEPT.LOC='SEVILLA';
--No es obligatorio poner el nombre de la tabla 
--de dónde recuperamos los datos ni en select ni 
--en where
select APELLIDO, OFICIO
, DNOMBRE, LOC, DEPT.DEPT_NO
from EMP
inner join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO
where LOC='SEVILLA';
--Alias en nombre de tabla
select e.APELLIDO, e.OFICIO
, d.DNOMBRE, d.LOC
from EMP e
inner join DEPT d
on e.DEPT_NO = d.DEPT_NO
where d.LOC='SEVILLA';
--Quiero visualizar el Apellido, Especialidad
--, Nombre de Hospital, Dirección de Hospital
--de los Doctores
select DOCTOR.APELLIDO, DOCTOR.ESPECIALIDAD
, HOSPITAL.NOMBRE, HOSPITAL.DIRECCION
from DOCTOR
inner join HOSPITAL
on DOCTOR.HOSPITAL_COD = HOSPITAL.HOSPITAL_COD;
--Mostrar el número de personas por cada departamento
--de los Empleados
select count(*) as PERSONAS, DEPT_NO
from EMP
group by DEPT_NO;
--Mostrar el número de personas por cada nombre de departamento
--de los empleados
select count(*) as PERSONAS, DEPT.DNOMBRE
from EMP
inner join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO
group by DEPT.DNOMBRE;

select distinct DEPT_NO from EMP;
select * from DEPT;
--Mostrar el Apellido, Oficio, Nombre de departamento, Localidad
--de los empleados.
--Solo los que combinen
select EMP.APELLIDO, EMP.OFICIO
, DEPT.DNOMBRE, DEPT.LOC
from EMP
inner join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO; 
--LEFT JOIN: ALUMNO AVIADOR
select EMP.APELLIDO, EMP.OFICIO
, DEPT.DNOMBRE, DEPT.LOC
from EMP
left join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO; 
--RIGHT JOIN: PRODUCCION GRANADA
select EMP.APELLIDO, EMP.OFICIO
, DEPT.DNOMBRE, DEPT.LOC
from EMP
right join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO; 
--FULL JOIN: PRODUCCION GRANADA
--ALUMNO AVIADOR
select EMP.APELLIDO, EMP.OFICIO
, DEPT.DNOMBRE, DEPT.LOC
from EMP
full join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO; 
--CROSS JOIN: Producto cartesiano
select EMP.APELLIDO, EMP.OFICIO
, DEPT.DNOMBRE, DEPT.LOC
from EMP
cross join DEPT;
--Quiero visualizar la suma salarial de la PLANTILLA 
--por cada Nombre de Hospital.
select sum(PLANTILLA.SALARIO) as SUMASALARIAL, HOSPITAL.NOMBRE
from PLANTILLA
inner join HOSPITAL
on PLANTILLA.HOSPITAL_COD = HOSPITAL.HOSPITAL_COD
group by HOSPITAL.NOMBRE;
--Quiero el número de empleados que trabajan en cada Localidad.
select count(EMP.EMP_NO) as EMPLEADOS, DEPT.LOC
from EMP
right join DEPT
on EMP.DEPT_NO = DEPT.DEPT_NO
group by DEPT.LOC;
--Mostrar el Apellido, Función, Nombre de hospital, 
--dirección del hospital 
--y nombre de sala de los empleados de la Plantilla.
select PLANTILLA.APELLIDO, PLANTILLA.FUNCION
, HOSPITAL.NOMBRE, HOSPITAL.DIRECCION
, SALA.NOMBRE
from PLANTILLA
inner join HOSPITAL
on PLANTILLA.HOSPITAL_COD=HOSPITAL.HOSPITAL_COD
inner join SALA
on HOSPITAL.HOSPITAL_COD=SALA.HOSPITAL_COD
and PLANTILLA.SALA_COD=SALA.SALA_COD;