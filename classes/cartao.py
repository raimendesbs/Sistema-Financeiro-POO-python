from datetime import date 
import json

class cartao:
    data_atual = date.today()
    def __init__(self, nome='', limite=0, vencimento=data_atual):
        self.nome = nome
        self.limite = limite
        self.vencimento = vencimento

        self.gastos = {}


    def adicionar_gasto(self, gasto):
        self.gastos.append(gasto)
        

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

def salvar_cartoes():
    with open("dados/cartoes.json", "w", encoding="utf-8") as arquivo:
        json.dump(cartao.to_dict(), arquivo, indent=4, ensure_ascii=False)

def carregar_cartoes():
    #ler os dados
    with open("dados/cartoes.json", "r", encoding="utf-8") as arquivo:
        dados_cartoes = json.load(arquivo)


nome = input("NOME DO CARTÃO: ")
limite = float(input('VALOR DO LIMITE DO CARTÃO: '))
vencimento = input("DATA DO VENCIMENTO: ")

card = cartao(nome, limite, vencimento)