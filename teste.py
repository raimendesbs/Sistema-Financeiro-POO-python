from datetime import date 

class gastos:
    data_atual = date.today()
    def __init__(self, descricao='', tipo='', valor=0, modalidade='credito' or 'debito', data=data_atual):
        self.descricao = descricao
        self.tipo = tipo
        self.valor = valor
        self.modalidade = modalidade
        self.data = data


    def __str__(self):
        return (
            f"Descrição: {self.descricao}\n"
            f"Tipo: {self.tipo}\n "
            f"Valor: {self.valor }\n"
            f"Modalidade de pagamento: {self.modalidade}\n "
            f"Data: {self.data}\n "
        )
    

modalidade = input('MODALIDADE: ')
descricao = input('DESCRIÇÃO: ')
tipo = input('CATEGORIA: ')
valor = float(input('VALOR: '))
data = input("DATA: ")


gasto1 = gastos()
gasto1.modalidade = input('MODALIDADE: ')
gasto1.descricao = descricao
gasto1.tipo = tipo
gasto1.valor = valor
gasto1.data = data

print(gasto1)