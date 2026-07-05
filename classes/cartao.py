from datetime import date 
import json
from gasto_cartao import objeto_gasto_cartao

class cartao:
    data_atual = date.today()
    def __init__(self, nome='', limite=0, vencimento=data_atual):
        self.nome = nome
        self.limite = limite
        self.vencimento = vencimento

        self.gastos = {}
        self.id = 1
    
    def adicionar_gasto(self):
        chave = self.id
        self.gastos[chave] = objeto_gasto_cartao(chave)

        self.id = self.id + 1
        print(f"Gasto salvo com sucesso no ID {chave}!")



    def calcular_fatura(self):
        total = 0 
        for gasto in self.gastos:
            total = total + gasto
        return total 
    

    def consultar_limite(self, limite):  
        total_fatura = self.calcular_fatura()  # 2. Faltava o 'self.' para chamar o método
        limite_restante = limite - total_fatura

        return limite_restante
    


    def exibir_fatura(self):
        for gasto in self.gastos:
            print(gasto)
        
        print(f"TOTAL DA FATURA: {self.calcular_fatura}")
    


    def to_dict(self):
        return {
            "nome": self.nome,
            "limite": self.limite,
            "vencimento": self.vencimento
            
        }


def objeto_cartao():
    nome = input("NOME DO CARTÃO: ")
    limite = float(input('VALOR DO LIMITE DO CARTÃO: '))
    vencimento = input("DATA DO VENCIMENTO: ")

    return cartao(nome, limite, vencimento)

card = objeto_gasto()


def salvar_cartoes():
    with open("dados/cartoes.json", "w", encoding="utf-8") as arquivo:
        json.dump(card.to_dict(), arquivo, indent=4, ensure_ascii=False)

def carregar_cartoes():
    #ler os dados
    with open("dados/cartoes.json", "r", encoding="utf-8") as arquivo:
        dados_cartoes = json.load(arquivo)

