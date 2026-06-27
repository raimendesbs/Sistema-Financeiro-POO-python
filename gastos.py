from datetime import date 

class gastos:
    data_atual = date.today()
    def __init__(self, descricao='', tipo='', valor=0, modalidade='', data=data_atual):
        self.descricao = descricao
        self.tipo = tipo
        self.valor = valor
        self.modalidade = modalidade
        self.data = data


    def __str__(self):
        return (
            f"Descrição: {self.descricao}"
            f"Tipo: {self.tipo}"
            f"Valor: {self.valor}"
            f"Modalidade de pagamento: {self.modalidade}"
            f"Data: {self.data}"
        )
