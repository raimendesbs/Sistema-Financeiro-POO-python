from datetime import date 
import json

class receitas:

    data_atual = date.today()
    def __init__(self, descricao='', tipo='', valor=0, data=data_atual):
        self.descricao = descricao
        self.tipo = tipo
        self.valor = valor
        self.data = data
        

    def to_dict(self):
        return {
            "Conta": self.conta,
            "Descrição": self.descricao,
            "Tipo": self.tipo,
            "Valor": self.valor,
            "Data": self.data
        }


    def __str__(self):
        return (
            f"Descrição: {self.descricao}"
            f"Tipo: {self.tipo}"
            f"Valor: {self.valor}"
            f"Data: {self.data}"
        )
    
def salvar_receitas():
    with open("dados/gastos.json", "w", encoding="utf-8") as arquivo:
        json.dump(receitas.to_dict(), arquivo, indent=4, ensure_ascii=False)

def carregar_receitas():
    #ler os dados
    with open("dados/receitas.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)



#CRIA UM OBJETO
descricao = input("DESCRIÇÃO: ")
tipo = input("TIPO: ")
valor = float(input("VALOR: "))
data = input("DATA: ")

receita = receitas(
    descricao,
    tipo,
    valor,
    data,
)