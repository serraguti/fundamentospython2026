print("Ejemplos clase STRING")
texto = "primero pYthon"
#VAMOS A IR PROBANDO DIFENTES METODOS
print("upper ", texto.upper())
print("lower ", texto.lower())
print("replace ", texto.replace("o", "@"))
print("Letra 0: ", texto[0])
print("Longitud: ", len(texto))
print("find(p): ", texto.find("p"))
print("find(z): ", texto.find("z"))
# texto.find("p",1)
# texto.find("p",upper)
# texto.find("p",lower)
#SOBRECARGA DE UN METODO
print("find(p, index): ", texto.find("p", 1))
print("rfind(p): ", texto.rfind("p"))
print("startswith(a) ", texto.startswith("a"))
print("endswith(n): ", texto.endswith("n"))
print("isdigit() ", texto.isdigit())
print("isalpha() ", texto.isalpha())
print("isalnum() ", texto.isalnum()) #letras y numeros
#Probamos SLICING, llamado Substring
#Recuperar una parte de un texto
subcadena = texto[2: ]
print("texto[2:]: ", subcadena)
#En python tambien podemos recuperar desde una posicion 
#hasta otra posicion
subcadena = texto[2: 5]
print("texto[2:5] ", subcadena)
#Podemos recorrer cada caracter con un bucle
longitud = len(texto) 
for i in range(longitud):
    letra = texto[i]
    print("letra[" + str(i) + "] = " + letra)
#Incluso podemos validar lo que nos ofrece un usuario...
print("Introduce un numero")
dato = input()  #"22"
if (dato.isdigit() == True):
    print("Me has dado un numero")
else:
    print("Que me des un numero!!!")


