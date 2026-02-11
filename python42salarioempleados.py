import oracledb

connection = oracledb.connect(user="system", password="oracle"
                              , dsn="localhost/FREEPDB1")
cursor = connection.cursor()
print("Oficio: ")
oficio = input()
print("Incremento salarial: ")
incremento = int(input())
sql = "update EMP set SALARIO = SALARIO + :dato1 where OFICIO=:dato2"
#de izquierda a derecha, buscara dentro de la consulta los :
cursor.execute(sql, (incremento, oficio,))
registros = cursor.rowcount
connection.commit()
print(f"Empleados afectados: {registros}")
sql = "select * from EMP where OFICIO=:inventado"
cursor.execute(sql, (oficio,))
for row in cursor:
    print(f"{row[1]}, Salario: {row[5]}")
cursor.close()
connection.close()
print("Fin de programa")