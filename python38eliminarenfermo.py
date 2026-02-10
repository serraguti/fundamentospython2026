import oracledb

connection = oracledb.connect(user="system", password="oracle"
                              , dsn="localhost/FREEPDB1")
#Creamos un solo cursor
cursor = connection.cursor()
#antes mostramos los enfermos (apellido, inscripcion)
sql = "select APELLIDO, INSCRIPCION from ENFERMO";
cursor.execute(sql)
for row in cursor:
    print(row[0] + ", Inscripcion: " + str(row[1]))
#cursor.close()
print("Introduzca inscripcion para eliminar: ")
dato = input()
sql = "delete from ENFERMO where INSCRIPCION=" + dato
cursor.execute(sql)
#Como es una consulta de acción, simplemente dibujamos
#los registros eliminados
afectados = cursor.rowcount
print("Registros eliminados: " + str(afectados))
#Realizamos los cambios permanentes
connection.commit()
cursor.close()
connection.close()
print("Fin de programa")