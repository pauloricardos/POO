class Servidor:
    def __init__(self, nome):
        self.nome = nome
        self.dicClientes = {}
        self.mensagens = []

    #método de acesso
    def getNome(self):
        return self.nome

    def getMensagens(self):
        return self.mensagens

    #outros métodos
    def cadastrarCliente(self, cliente):
        #A chave é o login do cliente e o valor é o objeto
        self.dicClientes[ cliente.getLogin() ] = cliente

    def receberMensagem(self, mensagem, senha):
        #checar autenticidade
        login = mensagem.getRemetente()
        cliente = self.dicClientes[ login ]
        if cliente.getSenha() == senha:
            self.mensagens.append(mensagem)
        
    def retornarNovaMensagem(self, login, senha):
        #checar autenticidade
        cliente = self.dicClientes[ login ]
        if cliente.getSenha() == senha:
            for m in self.mensagens:
                if login == m.getDestinatario() \
                   and m.getFoiLida() == False:
                    m.setFoiLida(True)
                    return m
            return None
    

    def retornarMensagem(self, indice, login, senha):
        cliente = self.dicClientes[ login ]
        if cliente.getSenha() == senha:
            for indice in self.mensagens:
                if login == indice.getDestinatario() \
                    and indice.getFoiLida() == False:
                    indice.setFoiLida(True)
                    return indice
            return None      