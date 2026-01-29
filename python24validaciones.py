import libreria24validaciones
print("Main de validaciones")
print("Introduzca ISBN")
isbn = input()
respuesta = libreria24validaciones.validarISBN(isbn) #???
if (respuesta == True):
    print("El ISBN esta BIEN")
else:
    print("El isbn no es correcto")
print("Fin del programa Main")