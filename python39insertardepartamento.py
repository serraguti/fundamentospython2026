import oracledb
connection = oracledb.connect(user="system", password="oracle"
                              , dsn="localhost/FREEPDB1")
#Creamos nuestro cursor para las consultas
cursor = connection.cursor() 
print("Id departamento")
id = input() #88
print("Nombre departamento")
nombre= input() #NUEVO
print("Localidad")
localidad = input() #LOC
#EN PYTHON TENEMOS UNA FORMA DE CONCATENAR TAMBIEN
#UTILIZANDO SOLAMENTE UN STRING, SIN + Y SIN NADA
#PARA ELLO, SE UTILIZA LA LETRA f FUERA DEL STRING
#Y CADA VARIABLE IRA ENTRE LLAVES DENTRO DEL STRING
sql = f"insert into DEPT values ({id},'{nombre}', '{localidad}')"
#Realizamos la acción de insertar
cursor.execute(sql)
connection.commit()
#Realizamos la consulta de seleccion
sql = "select * from DEPT"
cursor.execute(sql)
for row in cursor:
    num = row[0]
    nom = row[1]
    loc = row[2]
    print(f"Id: {num}, Nombre: {nom}, Localidad: {loc}")
cursor.close()
connection.close()
print("Fin de programa")