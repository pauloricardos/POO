class ObjetoGrafico(object):
    def __init__ (self, corDePreenchimento, preenchida, corDeContorno):
        self.corDePreenchimento = corDePreenchimento
        self.preenchida = preenchida
        self.corDeContorno = corDeContorno

class Retangulo(ObjetoGrafico):
    def __init__ (self, corDePreenchimento, preenchida, corDeContorno, base, altura):
        super(Retangulo, self).__init__(corDePreenchimento, preenchida, corDeContorno)
        self.base = base 
        self.altura = altura

    def calcArea(self):
        return self.base * self.altura
        

    def calcPerimetro(self):
       return 2 * (self.base * self.altura) 

from math import pi
class Circulo(ObjetoGrafico):
    def __init__ (self, corDePreenchimento, preenchida, corDeContorno, raio):
        super(Circulo, self).__init__(corDePreenchimento, preenchida, corDeContorno)
        self.raio = raio

    def calcArea(self):
        return pi * (self.raio * self.raio)     
        

    def calcPerimetro(self):
        return (2 * pi) * self.raio

class Triangulo(ObjetoGrafico):
    def __init__ (self, corDePreenchimento, preenchida, corDeContorno, base, altura):
        super(Triangulo, self).__init__(corDePreenchimento, preenchida, corDeContorno)
        self.base = base 
        self.altura = altura

    def calcArea(self):
        return (self.base * self.altura) / 2

    def calcPerimetro(self): 
        return 3 * self.base

triangulo = Triangulo("verde", True, "laranja", 5, 3)
print(triangulo.calcPerimetro())
print(triangulo.calcArea()) 

circulo = Circulo("azul", False, "vermelho", 3)
print(circulo.calcArea())
print(circulo.calcPerimetro())

retangulo = Retangulo("amarelo", True, "laranja", 3, 7)
print(retangulo.calcPerimetro())
print(retangulo.calcArea())
obj = ObjetoGrafico("azul", True, "verde")