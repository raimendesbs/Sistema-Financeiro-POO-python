from datetime import date

class cartao:
    
    def __init__(self, nome='', vencimento=''): 
        self.nome = nome
        self.vencimento = vencimento

    saldo = 0

    
class gastos:

    data_atual = date.today() 

    def __init__(self, descricao='', tipo='', valor=0, modalidade='CREDITO', data=data_atual, conta=''):
        self.descricao = descricao
        self.tipo = tipo
        self.valor = valor
        self.modalidade = modalidade
        self.data = data
        self.conta = conta


class receitas:
    def __init__(self, descricao='', tipo='', valor=0, conta=''):
        self.descricao = descricao
        self.tipo = tipo
        self.valor = valor
        self.conta = conta



class reserva:
    def __init__(self, nome='', valor_inicial=0, conta=''):
        self.nome = nome
        self.valor_incial = valor_inicial

    def deposito(saldo):
        deposito = int(input('VALOR A SER DEPOSITADO: '))
        saldo = saldo + deposito 



class conta:
    def __init__(self, nome=''):
        self.nome = nome

    saldo = 0
    