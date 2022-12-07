class CasaApostas:

    def __init__(self, nome, CNPJ, link):
        self.nome = nome
        self.CNPJ = CNPJ
        self.link = link 
        self.clientes = []
        self.apostas = []

class Cliente:
    
    def __init__(self, nome, CPF, conta):
        self.nome = nome
        self.CPF = CPF
        self.conta = conta 
        self.apostas = []

class Conta:

    def __init__(self, codigo_banco, agencia, numero):
        self.codigo_banco = codigo_banco
        self.agencia = agencia
        self.numero = numero

class Evento:
    def __init__(self, nome, finito):
        self.nome = nome
        self.finito = finito




