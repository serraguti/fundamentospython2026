print("Validar ISBN")
print("Introduzca ISBN")
isbn = input()
if (len(isbn) != 10):
    print("El ISBN debe tener 10 caracteres")
else:
    suma = 0
    for i in range(len(isbn)):
        #recuperamos cada caracter
        caracter = isbn[i]
        #convertimos a numero el caracter
        numero = int(caracter)
        multi = numero * (i + 1)
        suma = suma + multi
    #Preguntamos si la suma es divisible entre 11
    if (suma % 11 == 0):
        print("Numero ISBN correcto")
    else:
        print("El número introducido no es ISBN")
print("Fin de programa") 