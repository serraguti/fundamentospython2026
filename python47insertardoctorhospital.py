import oracledb

connection = oracledb.connect(user="system", password="oracle"
                              , dsn="localhost/FREEPDB1")
cursor = connection.cursor()
sql = "select max(DOCTOR_NO) + 1 as MAXIMO from DOCTOR"
cursor.execute(sql)
row = cursor.fetchone()
iddoctor = row[0]
#Comenzamos a pedir datos al usuario
apellido = input("Introduzca apellido: ")
espe = input("Especialidad: ")
salario = int(input("Salario doctor: "))
#Necesitamos mostrar los hospitales.
#lo que nos interesa son los códigos de hospital
print("Debe seleccionar un hospital a continuación")
sql = "select NOMBRE, HOSPITAL_COD from HOSPITAL"
cursor.execute(sql)
listaCodigos = []
contador = 1
for row in cursor:
    print(f"{contador}.- {row[0]}")
    listaCodigos.append(row[1])
    contador = contador + 1
print("Seleccione un hospital")
opcion = int(input())
idHospital = listaCodigos[opcion - 1]
sql = "insert into DOCTOR values (:hosp,:id,:ape,:espe,:sal)"
cursor.execute(sql, (idHospital,iddoctor,apellido,espe,salario,))
connection.commit()
print("Doctor insertado")
cursor.close()
connection.close()
print("Fin de programa")

