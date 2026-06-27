from datetime import date 

class SistemaFinanceiro:
    def __init__(self):
        self.contas = []


class Conta:

    def __init__(self, id, banco, apelido):
        self.id = id
        self.banco = banco
        self.apelido = apelido

        # Saldo atual da conta
        self.saldo = 0

        self.gastos = []
        self.receitas = []
        self.cartoes = []
        self.reservas = []

        '''METEODOS
        
        def criar_receita
        
        adicionar_receita
        
        adicionar_cartão
        
        criar_reserva
        
        exibir extrato
        
        consultar saldo'''




class gastos:
    data_atual = date.today()
    def __init__(self, descricao='', tipo='', valor=0, modalidade='', data=data_atual, id=0):
        self.descricao = descricao
        self.tipo = tipo
        self.valor = valor
        self.modalidade = modalidade
        self.data = data
        self.id = id


class receitas:
    data_atual = date.today()
    def __init__(self, descricao='', tipo='', valor=0, data=data_atual, id=0):
        self.descricao = descricao
        self.tipo = tipo
        self.valor = valor
        self.data = data
        self.id = id

class cartao:
    data_atual = date.today()
    def __init__(self, id, nome='', limite=0, vencimento=data_atual):
        self.id = id
        self.nome = nome
        self.limite = limite
        self.vencimento = vencimento

        self.gastos = []
    

    ''' METEODOS 
    adicionar_gasto()

        consultar_limite_restante()

        exibir_fatura()

        excluir_gasto()'''
    

class gastoCartao:
    data_atual = date.today()
    def __init__(self, id, descricao, tipo, valor, data=data_atual, parcelas=1, parcela_atual=1):
        self.id = id
        self.descricao = descricao
        self.tipo = tipo 
        self.valor = valor
        self.data = data 
        self.parcelas = parcelas
        self.parcela_atual = parcela_atual

class reserva:
    def __init__(self, id, saldo=0, nome=''):
        self.id = id
        self.saldo = saldo
        self.nome = nome 

    '''meteodos
    depositar()
    sacar()
    consultar_saldo()'''

