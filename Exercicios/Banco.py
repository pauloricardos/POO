class Banco(object):
    __total = 10000
    TaxaReserva = 0.1
    reservaExigida = __total*TaxaReserva
 
    def podeFazerEmprestimo(valor):
        Banco.__total -= valor
        if Banco.__total >= Banco.reservaExigida:
            pode = True
        else:
            pode = False
 
        Banco.__total += valor
 
        return pode
 
    def mudaTotal(valor):
        Banco.__total += valor
 
class Conta:
    def __init__(self, saldo, ID, senha):
        self.__saldo = saldo
        self.__ID = ID
        self.__senha = senha
 
    def deposito(self, senha, valor):
        if senha == self.__senha:
            self.__saldo += valor
            Banco.mudaTotal(valor)
 
    def saque(self, senha, valor):
        if senha == self.__senha:
            self.__saldo -= valor
            Banco.mudaTotal(-valor)
 
    def podeReceberEmprestimo(self, valor):
        return Banco.podeFazerEmprestimo(valor)
 
    def saldo(self):
        print(self.__saldo)