print("Mayor de tres numeros")
print("Primer numero")
num1  = int(input())
#directamente pedimos y guardamos
num2 = int(input("Numero dos: "))
num3 = int(input("Numero tres: "))
#organizar nuestro codigo
#las variables mejor no dejarlas en el programa por ahi tiradas
mayor = 0
menor = 0
intermedio = 0
if (num1 > num2 and num1 > num3):
    mayor = num1
elif (num2 > num1 and num2 > num3):
    mayor = num2
else:
    mayor = num3
#recuperamos el menor
if (num1 < num2 and num1 < num3):
    menor = num1
elif (num2 < num1 and num2 < num3):
    menor = num2
else:
    menor = num3
#6 , 4 , 2
# mayor: 6
# menor: 2
# 6 + 4 + 2 = 12
# 12 - 6 - 2 = 4
suma = num1 + num2 + num3
intermedio = suma - mayor - menor
print("Mayor ", mayor)
print("Menor ", menor)
print("Intermedio ", intermedio)
print("Fin de programa")
