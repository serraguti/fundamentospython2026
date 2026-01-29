def validarDni(dni): #12345678Z
    #separamos el numero de la letra que nos han dado
    numeros = dni[0: len(dni) - 1]
    letraEscrita = dni[len(dni) -1 :]
    numeros = int(numeros)
    letraCorrecta = getLetraDni(numeros)
    if (letraCorrecta.upper() == letraEscrita.upper()):
        return True
    else:
        return False

def getLetraDni(numeroDni):
    resultado = numeroDni - (int(numeroDni / 23) * 23)
    muestraLetras = "TRWAGMYFPDXBNJZSQVHLCKET";
    letra = muestraLetras[resultado]
    return letra

def validarISBN(isbn):
    if (len(isbn) != 10):
        return False
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
            return True
        else:
            return False
 