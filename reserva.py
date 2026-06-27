class Reserva:

    def __init__(self, id, nome):

        self.id = id
        self.nome = nome
        self.saldo = 0.0

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
