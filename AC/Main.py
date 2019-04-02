from Cliente import Cliente
from Servidor import Servidor
from Mensagem import Mensagem

s = Servidor('gmail')
c = Cliente('Josimar', '123456', s)

s.cadastrarCliente(c)
c = Cliente('Yohane', '345678', s)
s.cadastrarCliente(c)
m = Mensagem('Josimar', 'Yohane', 'Aula do Menezes', \
             'Yohane, hoje a aula vai ser maneira!!!!!')
s.receberMensagem(m, '123456') #senha correta
print("Primeiro envio: tamanho da lista = ", len(s.getMensagens()))

s.receberMensagem(m, '123') #senha errada
print("Segundo envio: tamanho da lista = ", len(s.getMensagens()))

print('Verificando a mensagen não lida da Yohane:')
print(s.retornarNovaMensagem('Yohane', '345678'))

print('Verificando novamente:')
print(s.retornarNovaMensagem('Yohane', '345678'))

print(s.retornarMensagem("indice", 'Josimar', '123456'))