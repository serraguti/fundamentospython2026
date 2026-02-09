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
row = cursor.fetchone() #Primera fila
print(row)
row = cursor.fetchone() #Segunda fila
print(row)
row = cursor.fetchone() #Tercera fila
print(row)
row = cursor.fetchone() #Cuarta fila
print(row)
#Qué sucede si leemos una fila cuando no tenemos más?
row = cursor.fetchone()
print(row)
#Siempre que finalicemos las acciones, debemos
#liberar los recursos
cursor.close()
connection.close()
print("Fin de programa")