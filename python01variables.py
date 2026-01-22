#Comentarios en Python
#Option derecha y 3
#Dibujar por pantalla es con string/texto
print ("Mi primer Python")
#Cada instruccion en una linea
#Declara variables: simplemente nos inventamos un nombre
nombre = "Paco"
numero = 14
numero2 = 6
suma = numero + numero2
resta = numero - numero2
division = numero / numero2
multi = numero * numero2
print ("Suma: ", suma)
print("Resta: ", resta)
print("Division ", division)
print("Multiplicacion ", multi)


print (nombre)
print (numero)
#Podemos representar variables junto a texto literal
print ("Su nombre es " + nombre)
print ("El numero es ", numero)
#Las variables tienen un tipo de dato interno
#Si intentamos concatenar un texto con un numero con +
print ("Su numero es " + str(numero))