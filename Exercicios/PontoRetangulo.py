class Ponto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def imprimir(self):
        print(self.x)
        print(self.y)

class Retangulo:
    def __init__ (self, ponto = Ponto(), altura = 0, largura = 0):
        self.altura = altura
        self.largura = largura
        self.vertice = ponto

    def calcCentro(self):
       x = (self.vertice.x + self.largura)/2
       y = (self.vertice.y + self.largura)/2
       return (Ponto(x, y))

vertice = Ponto(10, 30)
rect = Retangulo(vertice, 31, 10)
vertice.imprimir()
print(rect.calcCentro())
