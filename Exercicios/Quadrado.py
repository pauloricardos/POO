class Quadrado:
    def __init__ (self, tamanhoLado):
        self.tamanhoLado = tamanhoLado

    def calcularArea(self):
        area = self.tamanhoLado * self.tamanhoLado  
        self.area = area
        return self.area
          

calcArea = Quadrado(30)
print(calcArea.calcularArea())