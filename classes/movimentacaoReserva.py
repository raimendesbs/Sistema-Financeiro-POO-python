from datetime import date

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
            f"{self.data} | "
            f"{self.tipo} | "
            f"{self.descricao} | "
            f"R$ {self.valor:.2f}"
        )
    