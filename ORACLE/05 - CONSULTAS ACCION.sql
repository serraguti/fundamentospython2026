select * from PLANTILLA;
select max(EMPLEADO_NO) + 1 from PLANTILLA;
--9902
commit;
insert into PLANTILLA
(HOSPITAL_COD, SALA_COD, APELLIDO
, FUNCION, TURNO, SALARIO, EMPLEADO_NO)
values (22, 6, 'Super Lopez', 'ENFERMERA', 'T', 150000
, (select max(EMPLEADO_NO) + 1 from PLANTILLA));
delete from PLANTILLA;
ROLLBACK;
delete from PLANTILLA where apellido='Super Lopez';
--Eliminar toda la plantilla del hospital El Carmen
delete from PLANTILLA where HOSPITAL_COD=
(select HOSPITAL_COD from HOSPITAL where NOMBRE='El Carmen');
--subir en 1 el salario de la plantilla (todos)
update PLANTILLA set SALARIO = SALARIO + 1;
update PLANTILLA set funcion='ENFERMERA', SALARIO=SALARIO + 1
where FUNCION='ENFERMERO';
update PLANTILLA set SALARIO=
(select SALARIO from PLANTILLA where APELLIDO='karplus w.')
where SALA_COD=4;
select SALARIO from PLANTILLA where APELLIDO='karlus w.';
--Mostrar todas las personas de la PLANTILLA de la 
--sala de psiquiatria
select * from PLANTILLA
where SALA_COD in
(select SALA_COD from SALA where NOMBRE='psiquiatria');
select SALA_COD from SALA where NOMBRE='psiquiatria';
--Modificar el TURNO a Mañana a todos los de la plantilla
--de la sala de Psiquiatría
update PLANTILLA set TURNO='M'
where SALA_COD in 
(select SALA_COD from SALA where NOMBRE='psiquiatria');
select SALA_COD from SALA where NOMBRE='psiquiatria';
select * from SALA;
--Insertar un nuevo empleado de la Plantilla.
--Su nombre es CABRALES, Sala 4, Turno N 
--y trabajará en el Hospital El Carmen.
--El Id debemos buscar el máximo libre.
insert into PLANTILLA
(HOSPITAL_COD, SALA_COD, APELLIDO, TURNO, EMPLEADO_NO)
values
(null
, 4, 'CABRALES', 'M',
(select max(EMPLEADO_NO) + 1 from PLANTILLA));
select * from PLANTILLA;
select * from PLANTILLA
where HOSPITAL_COD is null or 
HOSPITAL_COD not in (select HOSPITAL_COD from HOSPITAL);
rollback;
select * from HOSPITAL;
TRUNCATE TABLE HOSPITAL;
delete from HOSPITAL;
select * from PLANTILLA where HOSPITAL_COD=55;

