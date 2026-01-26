print("Sumar números usuario")
print("Introduzca un numero")
numero = int(input()) #5
contador = 1
suma = numero
while (numero != 0):
    print("Dame otro numero")
    numero = int(input()) #2
    suma = suma + numero
    contador = contador + 1
print("Números solicitados: ", contador)
print("Suma de numeros: ", suma)
print("Fin de programa")