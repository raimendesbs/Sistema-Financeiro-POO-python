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