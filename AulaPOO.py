class Cachorro:
    def __init__ (self, numero, nome, cor):
        self.numero = 30
        self.nome = 'Lenildo'
        self.cor = 'azul'

    def latir(self):
        print ("AUAUAUAU")   

Dog = Cachorro(5, 'Rex', 'Marrom')
print(Dog.nome)
print(Dog.numero)
print(Dog.cor)
Dog.latir()
