from class31coche import Coche

class Deportivo(Coche):
    def getVelocidadMaxima(self):
        velocidadCoche = super().getVelocidadMaxima()
        return velocidadCoche + 100
    
    def turbo(self):
        self.velocidad += 100
        print("Turbo a tope!!!!", self.velocidad)
    
    def acelerar(self):
        self.velocidad += 45
        print("Acelerando en deportivo!!! ", self.velocidad)