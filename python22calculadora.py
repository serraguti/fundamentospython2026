def sumarNumeros(num1, num2):
    suma = num1 + num2
    return suma
def restarNumeros(num1, num2):
    return num1 - num2
def multiplicarNumeros(num1, num2):
    return num1 * num2
def menuCalculadora():
    print("0.- Salir")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("Selecciona una opción")

#Programa principal MAIN
print("Programa calculadora")
print("Introduce numero 1")
numero1 = int(input())
print("Introduce numero 2")
numero2 = int(input())
#Quiero mostrar el menu calculadora, hasta cuando???
#Cuando el usuario ponga SALIR ( 0 ), salimos del bucle
#Vamos a dar un valor por defecto a opcion para que 
#entre en el bucle
opcion = -1
while (opcion != 0):
    menuCalculadora()
    opcion = int(input())
    operacion = 0
    if (opcion == 1):
        operacion = sumarNumeros(numero1, numero2)
    elif (opcion == 2):
        operacion = restarNumeros(numero1, numero2)
    elif (opcion == 3):
        operacion = multiplicarNumeros(numero1, numero2)
    else:
        print("Opción no valida")
    print("Operacion: ", operacion)
print("Fin de programa")
