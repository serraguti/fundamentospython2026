import oracledb

connection = oracledb.connect(user="system", password="oracle"
                              , dsn="localhost/FREEPDB1")
cursor = connection.cursor()
print("Hospital")
idhospital = int(input())
print("Incremento salarial")
incremento = int(input())
sql = "update PLANTILLA set SALARIO=SALARIO + :subida "\
    " where HOSPITAL_COD=:codigo"
cursor.execute(sql, (incremento, idhospital,))
connection.commit()
registros = cursor.rowcount
print(f"Salarios subidos {registros}") 
sql = "select * from PLANTILLA where HOSPITAL_COD=:codigo"
cursor.execute(sql, (idhospital,))
for row in cursor:
    print(f"{row[3]}, Salario: {row[6]}")
cursor.close()
connection.close()
print("Fin de programa")