print("Ejemplo listas")
numero = 0
suma = 0
sumaPares = 0
sumaImpares = 0
listaNumeros = []
listaPares = []
listaImpares = []
while (numero != -1):
    print("Introduzca un numero")
    numero = int(input())
    suma = suma + numero
    listaNumeros.append(numero)
    if (numero % 2 == 0):
        listaPares.append(numero)
        sumaPares = sumaPares + numero
    else:
        listaImpares.append(numero)
        sumaImpares = sumaImpares + numero
print("Datos de los numeros")
print("Numeros introducidos: ", len(listaNumeros))
print("Numeros Pares: ", len(listaPares))
print("Numeros impares: ", len(listaImpares))
print("Suma pares ", sumaPares)
print("Suma impares ", sumaImpares)
print("Suma total ", suma)
#Dibujar cada una de las listas
print("------Todos los numeros-----")
for num in listaNumeros:
    print(num) 
print("------Numeros impares-------")  
for num in listaImpares:
    print(num)
print("----Numeros Pares-------")
for num in listaPares:
    print(num)
print("Fin de programa") 
    