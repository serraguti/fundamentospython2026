print("Calcular dia semana")
print("Introduzca día de nacimiento")
dia = int(input())
print("Introduzca mes")
mes = int(input())
print("Su año de nacimiento")
anyo = int(input())
if (mes == 1):
    mes = 13
    anyo = anyo - 1
elif (mes == 2):
    mes = 14
    anyo = anyo - 1
#calculamos todo
ope1 = int(((mes+1) * 3) / 5)
ope2 = int(anyo / 4)
ope3 = int(anyo / 100)
ope4 = int(anyo / 400)
# Sumar el dia, el doble del mes, el año, 
# el resultado de la operación 1, 
# el resultado de la operación 2, 
# menos el resultado de la operación 3 
# más la operación 4 más 2. 
ope5 = dia  + (mes * 2) + anyo + ope1 + ope2 - ope3 + ope4 + 2
ope6 = int(ope5 / 7)
resultado = ope5 - (ope6 * 7)
if (resultado == 0):
    print("SABADO")
elif (resultado == 1):
    print("DOMINGO")
elif (resultado == 2):
    print("LUNES")
elif (resultado == 3):
    print("MARTES")
elif (resultado == 4):
    print("MIERCOLES")
elif (resultado == 5):
    print("JUEVES")
elif (resultado == 6):
    print("VIERNES")
print("Fin de programa")