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
    print("4.- Introducir nuevos números")
    print("Selecciona una opción")

#Creamos un metodo que devolverá el número introducido
#En este método, tendremos un bucle infinito hasta que
#nos de un número
def getNumero():
    print("Introduzca un número")
    #ALMACENAMOS LO QUE ESCRIBA EL USUARIO
    #EN UNA VARIABLE string
    aux = input()
    #Entramos en un bucle mientras que NO sean NUMEROS
    while (aux.isdigit() == False):
        print("Eso no era un numero")
        print("Introduzca número")
        aux = input()
    #Convertimos el texto a numero
    num = int(aux)
    #Devolvemos el numero desde el metodo
    return num