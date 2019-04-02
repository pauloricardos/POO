class Retangulo:
    def __init__ (self, weight, height):
        self.weight = weight
        self.height = height

    def setLados(self):
        pass

    def getLados(self):  
        return self.weight, self.height

    def calcArea(self):
        self.area = self.weight * self.height
        return self.area

    def calcPerimetro(self):
        self.perimeter = 2 * (self.height + self.weight)
        return self.perimeter
    
rectangle = Retangulo(120, 300)
print(rectangle.calcArea())
print(rectangle.calcPerimetro())
              