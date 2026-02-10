import oracledb

print("Conectando a Oracle")
#Tenemos un objeto connection que nos pedirá
#(user, password, server)
connection = oracledb.connect(user="SYSTEM"
                              , password="oracle"
                              , dsn="localhost/FREEPDB1")
print("Estamos conectados!!!!")
#Creamos nuestra consulta SQL con los departamentos
#La consulta SQL desde Python no finaliza en ;
sql = "select * from DEPT"
#Creamos un cursor para la consulta
cursor = connection.cursor()
#Debemos ejecutar la consulta para que nos devuelva los 
#datos de Oracle
cursor.execute(sql)
#Aqui ya estan los datos
#Una vez que tenemos el cursor, debemos leer los datos.
#Tenemos un método llamado fetchone() que se mueve una fila
#cada vez que lo ejecutamos
#Nos devuelve la fila en la que estamos posicionados.
#Comentarios en bloque VS Code
#Seleccionamos lo que deseemos comentar
#Comentar: Command/Control + k + c
#Descomentar: Command/Control + k + u
# row = cursor.fetchone() #Primera fila
# print(row)
# row = cursor.fetchone() #Segunda fila
# print(row)
# row = cursor.fetchone() #Tercera fila
# print(row)
# row = cursor.fetchone() #Cuarta fila
# print(row)
# #Qué sucede si leemos una fila cuando no tenemos más?
# row = cursor.fetchone()
# print(row)
#Si queremos leer todos los registros del cursor:
#1) while
# row = cursor.fetchone()
# while (row != None):
#     print("Leer filas...")
#     row = cursor.fetchone()
#2) for
# for row in cursor:
#     print(row)
#     #Tambien podemos extraer los datos de alguna
#     #columna mediante su indice
#     print(row[0]) #DEPT_NO
#     print(row[1]) #DNOMBRE
    #En algunas BBDD nos permite extraer el dato 
    #de la fila por el NOMBRE de la Columna
    #Oracle no contiene la info de las columnas
    # nombre = row.DNOMBRE
    # print(nombre)
#3) Recorrer con variables el cursor
#Nuestra consulta tiene 3 columnas
for numero, nombre, localidad in cursor:
    print(nombre) 
#No podemos leer las filas una vez que ya hemos leído el cursor
#tendríamos que volver a execute la consulta.
#Siempre que finalicemos las acciones, debemos
#liberar los recursos
cursor.close()
connection.close()
print("Fin de programa")