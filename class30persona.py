class Persona:
    #Podemos declarar las propiedades en el constructor
    #directamente e iniciarlas
    def __init__(self):
        self.nombre = ""
        self.apellidos = ""
        self.email = ""
        self.anyonacimiento = 0
        self.pais = "Francia"
    
    def __str__(self):
        return "Hoy es lunes, te estoy cambiando..."
    
    #Metodos son acciones sobre la clase Persona
    def getNombreCompleto(self):
        return self.nombre + " " + self.apellidos
    
    def getEdad(self):
        return 2026 - self.anyonacimiento
    
    def getEdadFalsa(self, añosquitados):
        return 2026 - self.anyonacimiento - añosquitados
