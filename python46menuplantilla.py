import oracledb

connection = oracledb.connect(user="system", password="oracle"
                              , dsn="localhost/FREEPDB1")
cursor = connection.cursor()
sql = "select distinct FUNCION from PLANTILLA"
listaFunciones = []
cursor.execute(sql)
contador = 1
for row in cursor:
    print(f"{contador}) {row[0]}")
    listaFunciones.append(row[0])
    contador = contador + 1
print("Seleccione una función: ")
opcion = int(input())
funcionSeleccionada = listaFunciones[opcion - 1]
sql = "select APELLIDO from PLANTILLA where FUNCION=:param"
cursor.execute(sql, (funcionSeleccionada,))
print("-----Plantilla------")
for row in cursor:
    print(f"- {row[0]}")
cursor.close()
connection.close()
print("Fin de programa")



