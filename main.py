from classes import gastos


funcionalidade = input(''' 
==================== MENU ===================
0 - EXIBIR INFORMAÇÕES GERAIS
1 - ADICIONAR GASTO 
2 - ADICIONAR RECEITA
3 - EXIBIR EXTRATO DA CONTA CORRENTE
4 - ADICIONAR CARTÃO DE CREDITO
5 - ADICIONAR GASTO NO CARTÃO DE CREDITO
6 - EXIBIR EXTRATO DO CARTÃO DE CREDITO
7 - ADICIONAR RESERVA
8 - EXIBIR EXTRATO DA RESERVA            
9 - FAZER DEPOSITO NA RESERVA ''')


if funcionalidade == 1:
    modalidade = input('MODALIDADE: ')
    descricao = input('DESCRIÇÃO: ')
    tipo = input('CATEGORIA: ')
    valor = float(input('VALOR: '))
    data = input("DATA: ")

