class SistemaFinanceiro:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


    def to_dict(self):

        return {

            "contas":[
                conta.to_dict()
                for conta in self.contas
            ]

        }