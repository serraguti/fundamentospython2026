import libreria29narcisista
print("Numero narcista")
print("Introduce un numero iniciar")
inicial = int(input())
print("Introduzca numero final")
final = int(input())
for inicial in range(inicial, final):
    if (libreria29narcisista.numeroNarcisista(inicial) == True):
        print(inicial)
print("Fin de programa")
