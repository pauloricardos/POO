class Pessoa:
    def __init__ (self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade 
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade+=anos
        self.peso = self.peso + 1 * anos
        if self.idade < 21:
            self.altura+=0.05
        return self.idade    

    def engordar(self, kilos):
        self.peso += kilos
        return self.peso

    def emagrecer(self, kilos):   
        self.peso += kilos 
        return self.peso    

    def crescer(self, metros):    
        self.altura+= metros
        return self.altura   

pessoa = Pessoa("Anderson", 20, 50, 1.67)
print(pessoa.envelhecer(20))
print(pessoa.engordar(50))
print(pessoa.emagrecer(50))
print(pessoa.crescer(1.67))