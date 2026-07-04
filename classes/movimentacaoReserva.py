from datetime import date
import json
class MovimentacaoReserva:

    def __init__(self,
                 descricao,
                 tipo,
                 valor,
                 data=date.today()):

        self.descricao = descricao
        self.tipo = tipo
        self.valor = valor
        self.data = data

    def __str__(self):

        return (
            f" DATA: {self.data}"
            f"CATEGORIA: {self.tipo} | "
            f"DESCRIÇÃO: {self.descricao} | "
            f" VALOR: R${self.valor:.2f}"
        )
    
    def to_dict(self):
        return {
            "Descrição": self.descricao,
            "Tipo": self.tipo,
            "Valor": self.valor,
            "Data": self.data
        }
    
def salvar_movReserv():
    with open("dados/movimenta_reserva.json", "w", encoding="utf-8") as arquivo:
        json.dump(MovimentacaoReserva.to_dict(), arquivo, indent=4, ensure_ascii=False)

def carregar_movReserv():
    #ler os dados
    with open("dados/movimenta_reserva.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)



tipo = input('TIPO DE MOVIMENTAÇÃO: ')
valor = float(input('VALOR: '))
descricao = input('DESCRIÇÃO: ')
data = input('DATA: ')
movimentacao = MovimentacaoReserva(descricao, tipo, valor, data)