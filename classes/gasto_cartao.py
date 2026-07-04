from datetime import date
import json

class gastoCartao:
    data_atual = date.today()
    def __init__(self, descricao, tipo, valor, data=data_atual, parcelas=1, parcela_atual=1):
        self.id = id
        self.descricao = descricao
        self.tipo = tipo 
        self.valor = valor
        self.data = data 
        self.parcelas = parcelas
        self.parcela_atual = parcela_atual
    
    def to_dict(self):
        return {
            "Descrição": self.descricao,
            "Tipo": self.tipo,
            "Valor": self.valor,
            "Numero de Parcelas": self.parcelas,
            "Parcela atual": self.parcela_atual,
            "Data": self.data
        }


def salvar_gastos_cartoes():
    with open("dados/gastos.json", "w", encoding="utf-8") as arquivo:
        json.dump(gastoCartao.to_dict(), arquivo, indent=4, ensure_ascii=False)

def carregar_gastos_cartoes():
    #ler os dados
    with open("dados/gastos_cartao.json", "r", encoding="utf-8") as arquivo:
        gastos_cartoes = json.load(arquivo)


    
descricao = input("DESCRIÇÃO: ")
tipo = input("TIPO: ")
valor = float(input("VALOR: "))
parcelas = int(input("NÚMERO DE PARCELAS: "))
parcela_atual = int(input("PARCELA ATUAL: "))
data = input("DATA (AAAA-MM-DD): ")

despesaCartao = gastoCartao(
    id,
    descricao,
    tipo,
    valor,
    data,
    parcelas,
    parcela_atual
)





