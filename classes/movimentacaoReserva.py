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
            f" DATA: {self.data}"
            f"CATEGORIA: {self.tipo} | "
            f"DESCRIÇÃO: {self.descricao} | "
            f" VALOR: R${self.valor:.2f}"
        )
    
movimentacao = MovimentacaoReserva()
movimentacao.tipo = input('TIPO DE MOVIMENTAÇÃO: ')
movimentacao.valor = float(input('VALOR: '))
movimentacao.descricao = input('DESCRIÇÃO: ')
movimentacao.data = input('DATA: ')

