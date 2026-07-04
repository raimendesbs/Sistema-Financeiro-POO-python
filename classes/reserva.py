import movimentacaoReserva as mr
import json 

class Reserva:

    def __init__(self, nome):

        self.nome = nome
        self.saldo = 0
    

        self.movimentacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.movimentacoes.apped(valor)
        

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente na reserva.")
            return False

        self.saldo -= valor
        self.movimentacoes.append(valor)

        return True


    def consultar_saldo(self):
        return self.saldo

    def __str__(self):
        return (
            f"Reserva: {self.nome}\n"
            f"Saldo: R$ {self.saldo:.2f}"
        )

    def extrato(self): 
        for movimentacao in self.movimentacoes:
            print(self.movimentacao)
            print(f"SALDO TOTAL DA RESERVA: {self.consultar_saldo}")
    
    def to_dict(self):
        return {
            "nome": self.nome

        }


def salvar_reserva():
    with open("dados/gastos.json", "w", encoding="utf-8") as arquivo:
        json.dump(Reserva.to_dict(), arquivo, indent=4, ensure_ascii=False)

def carregar_reserva():
    #ler os dados
    with open("dados/reservas.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)



nome = input('NOME: ')
reserv = Reserva(nome)