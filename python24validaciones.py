import libreria24validaciones
print("Main de validaciones")
print("Introduzca un Dni")
dni = input()
respuesta = libreria24validaciones.validarDni(dni)
if (respuesta == True):
    print("El dni es correcto")
else:
    print("El dni es INCORRECTO")
#numDni = int(input())
#letra = libreria24validaciones.getLetraDni(numDni)
#print(letra) #Z

#separamos el numero de la letra que nos han dado

# print("Introduzca ISBN")
# isbn = input()
# respuesta = libreria24validaciones.validarISBN(isbn) #???
# if (respuesta == True):
#     print("El ISBN esta BIEN")
# else:
#     print("El isbn no es correcto")
print("Fin del programa Main")