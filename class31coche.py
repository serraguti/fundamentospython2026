class Coche:
    #Declaramos las propiedades en el constructor
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.velocidad = 0
        self.estado = False
    
    def getVelocidadMaxima(self):
        return 180
    
    
    def arrancar(self):
        self.estado = True
        print("Coche arrancado")
    
    def detener(self):
        self.estado = False
        print("Coche apagado")
    
    def acelerar(self):
        if (self.estado == False):
            print("Enciende el coche!!!, Ande vas!")
        else:
            self.velocidad = self.velocidad + 20
            print("Su velocidad es de ", self.velocidad)
    
    def frenar(self):
        if (self.velocidad == 0):
            print("Si ya estas parado....")
        else:
            self.velocidad = self.velocidad - 10
            print("Su velocidad es de ", self.velocidad)