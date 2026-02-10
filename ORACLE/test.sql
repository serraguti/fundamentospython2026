select * from DEPT;
select * from DEPT where DEPT_NO=1;
select APELLIDO, DIRECCION from ENFERMO where INSCRIPCION=10995;
select APELLIDO, FUNCION from PLANTILLA where TURNO='T';

delete from ENFERMO;
rollback;
