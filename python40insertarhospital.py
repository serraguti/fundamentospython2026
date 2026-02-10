import oracledb
connection = oracledb.connect(user="system", password="oracle"
                              , dsn="LOCALHOST/FREEPDB1")
cursor = connection.cursor()
print("Id de hospital")
id = input()
print("Nombre")
nombre = input()
print("Dirección del hospital")
direccion = input()
print("Teléfono")
tlf = input()
print("Número de camas")
camas = input()
sql = f"insert into HOSPITAL values({id},'{nombre}','{direccion}','{tlf}', {camas})"
cursor.execute(sql)
connection.commit()
sql = "select * from HOSPITAL"
cursor.execute(sql)
for row in cursor:
    print(f"Id: {row[0]}, Nombre: {row[1]}, Direccion: {row[2]}, Tlf: {row[3]}, Camas: {row[4]}")
cursor.close()
connection.close()
print("Fin de programa")