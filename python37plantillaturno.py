import oracledb

connection = oracledb.connect(user="system", password="oracle"
                              , dsn="localhost/FREEPDB1")
print("Dame un turno (T,M,N)")
turno = input()
sql = "select APELLIDO, FUNCION from PLANTILLA "\
    " where TURNO='" + turno + "'"
print(sql) #PINTAR LA CONSULTA QUE HACEMOS DINAMICAMENTE
cursor = connection.cursor()
cursor.execute(sql)
for row in cursor:
    apellido = row[0]
    funcion = row[1]
    print(apellido + ", " + funcion)
cursor.close()
connection.close()
print("Fin de programa")