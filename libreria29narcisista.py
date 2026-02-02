import math
def numeroNarcisista(narcisista):
    numeroTexto = str(narcisista)
    longitud = len(numeroTexto)
    suma = 0
    for i in range(longitud):
        letraNumero = numeroTexto[i]
        numero = int(letraNumero)
        potencia = math.pow(numero, longitud)
        suma = suma + potencia
    #Comprobamos los valores
    if (suma == narcisista):
        return True
    else:
        return False   