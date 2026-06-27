from datetime import date 

class receitas:
    data_atual = date.today()
    def __init__(self, descricao='', tipo='', valor=0, data=data_atual, id=0):
        self.descricao = descricao
        self.tipo = tipo
        self.valor = valor
        self.data = data
        self.id = id

        def __str__(self):
            return (
                f"Descrição: {self.descricao}"
                f"Tipo: {self.tipo}"
                f"Valor: {self.valor}"
                f"Data: {self.data}"
        )