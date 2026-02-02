from class30persona import Persona
print("Manejando clases persona")
#Creamos una persona
persona1 = Persona()
persona1.nombre = "Roger"
persona1.apellidos = "Rabbit"
persona1.anyonacimiento = 1989
persona1.pais = "EEUU"
print("Edad falsa: ", persona1.getEdadFalsa(10))
print(persona1.getNombreCompleto())
print("Edad persona 1: ", persona1.getEdad())
persona2 = Persona()
print(persona2)
print("Fin de programa")
