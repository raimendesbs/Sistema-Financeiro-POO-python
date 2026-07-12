from datetime import date 
import json

class gastos:
    data_atual = date.today()
    def __init__(self, id_gerado, descricao='', tipo='', valor=0, data=data_atual):
        self.id = id_gerado
        self.descricao = descricao
        self.tipo = tipo
        self.valor = valor
        self.data = data
        


    def __str__(self):
        return (
            f"Descrição: {self.descricao}"
            f"Tipo: {self.tipo}"
            f"Valor: {self.valor}"
            f"Data: {self.data}"
        )

    def to_dict(self):
        return {
            "Descrição": self.descricao,
            "Tipo": self.tipo,
            "Valor": self.valor,
            "Data": self.data
        }

#salvar dados
def objeto_gasto(id_atual):
    descricao = input("DESCRIÇÃO: ")
    tipo = input("TIPO: ")
    valor = float(input("VALOR: "))
    data = input("DATA: ")

    return gastos(
        id_atual,
        descricao,
        tipo,
        valor,
        data,
    )

despesa = objeto_gasto()


def salvar_gastos():
    with open("dados/gastos.json", "w", encoding="utf-8") as arquivo:
        json.dump(despesa.to_dict(), arquivo, indent=4, ensure_ascii=False)

def carregar_gastos():
    #ler os dados
    with open("dados/gastos.json", "r", encoding="utf-8") as arquivo:
        dados_gastos = json.load(arquivo)



