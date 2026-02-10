import oracledb
#Creamos conexion a oracle
connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
print("Conectado")
#Pedimos el departamento al usuario
print("Introduce un ID de departamento")
iddepartamento = input()
#Necesitamos una consulta para buscar un departamento
sql = "select * from DEPT where DEPT_NO=" + iddepartamento
print(sql)
#Creamos un cursor
cursor = connection.cursor()
#Ejecutamos la consulta para traer los datos
cursor.execute(sql)
#Recuperamos la primera fila
row = cursor.fetchone()
#Comprobamos si tenemos datos o no en la fila
if (row == None):
    print("No existe el departamento")
else:
    #Recuperamos los datos
    nombre = row[1] #DNOMBRE
    localidad = row[2] #LOC
    print(nombre + ", " + localidad)
#Liberamos los recursos
cursor.close()
connection.close()
print("Fin de programa")
