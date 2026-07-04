class Conta:

    def __init__(self, id, banco, apelido):
        self.id = id
        self.banco = banco
        self.apelido = apelido

        # Saldo atual da conta
        self.saldo = 0

        self.gastos = []
        self.receitas = []
        self.cartoes = []
        self.reservas = []

    
    def adicionar_receita(self, receita):
        self.receitas.append(receita)
        self.saldo = self.saldo + receita.valor

    def adicionar_gastos(self, gasto):
        self.gastos.append(gasto)
        self.saldo = self.saldo - gasto.valor

    def adicionar_cartoes(self, cartao):
        self.cartoes.append(cartao)

    def adicionar_reserva(self, reserva):
        self.reserva.append(reserva)

    def exibir_extrato(self):

        print(f"Banco: {self.banco}")
        print(f"Saldo: R$ {self.saldo:.2f}")

        print("\nReceitas")
        for receita in self.receitas:
            print(receita)

        print("\nGastos")
        for gasto in self.gastos:
            print(gasto)
