import oracledb
connection = oracledb.connect(user="system", password="oracle"
                              , dsn="localhost/FREEPDB1")
print("Introduzca inscripcion")
dato = input()
sql = "select APELLIDO, DIRECCION from ENFERMO "\
 " where INSCRIPCION="+dato
cursor = connection.cursor()
cursor.execute(sql)
row = cursor.fetchone()
if (row == None):
    print("No existen enfermos con esa inscripcion")
else:
    apellido = row[0]
    direccion = row[1]
    print(apellido + ", " + direccion)
cursor.close()
connection.close()
print("Fin de programa")