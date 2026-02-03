#https://fjtoscano.medium.com/instalar-oracle-database-xe-en-mac-m1-d5d2d17fc00c
class Mes:
    def __init__(self):
        self.nombre = ""
        self.temperaturaMinima = 0
        self.temperaturaMaxima = 0
    #Necesitamos un metodo para calcular la media de un mes
    def getTemperaturaMedia(self):
        media = (self.temperaturaMaxima + self.temperaturaMinima) / 2
        return media