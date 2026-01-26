print("Tabla multiplicar")
print("Introduce un numero")
numero = int(input())
for i in range(1, 11):
    resultado = numero * i
    print(str(numero) + "*" + str(i) + "=" + str(resultado))
print("Fin de programa")