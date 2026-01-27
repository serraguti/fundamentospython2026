#EN UN PROGRAMA QUE DESEAMOS EJECUTAR
#LOS METODOS SE ESCRIBEN AL INICIO
#LA SINTAXIS DE LOS METODOS SE ESCRIBE 
#CON LA SEGUNDA INICIAL Y SIGUIENTES EN MAYUSCULA
#  primer()
#  primerMetodo()
# primerMetodoMartes()
def primerMetodo():
    #ESTE CODIGO JAMAS SE EJECUTA
    #SI NO LO LLAMAMOS EXPLICITAMENTE
    print("Primer metodo")
def segundoMetodo():
    print("Segundo metodo")
def saludar(nombre):
    print("Bienvenido a Python Mr/Mrs " + nombre)
def despedirse(nombre, dia):
    print("Ha sido un placer hoy " + dia + ", Mr/Mrs " + nombre)
    
#ESTO ES MI PROGRAMA PRINCIPAL
print("Ejemplo de metodos")
#En el programa principal, llamamos a los metodos
saludar("Alumno")
primerMetodo()
segundoMetodo()
primerMetodo()
despedirse("Alumno", "Martes")
print("Fin de programa")