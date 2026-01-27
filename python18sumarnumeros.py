print("Sumar números letras")
print("Introduce una cifra")
textoNumeros = input()
#AVERIGUAMOS SI SON NUMEROS O NO
if (textoNumeros.isdigit() == False):
    print("Esto no son numeros: ", textoNumeros)
else:
    #1+2+3+4
    suma = 0
    #Recorremos cada caracter del texto
    for i in range(len(textoNumeros)):
        #Necesito cada letra del texto
        letra = textoNumeros[i] 
        #Convertimos la letra a numero
        numero = int(letra)
        suma = suma + numero
print("La suma de " + textoNumeros + " es " + str(suma))
print("Fin de programa")






