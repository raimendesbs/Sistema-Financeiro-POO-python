import cartao 
import receitas 
import gastos 
import reserva 

class contas:

    def __init__(self, banco, apelido):
        self.banco = banco
        self.apelido = apelido


        self.gastos = {}
        self.receitas = {}
        self.cartoes = {}
        self.reservas = {}

        self.id_gasto = 1
        self.id_receita = 1
        self.id_cartao = 1
            


    def adicionar_receita(self):
        chave = self.id_receita

        obj_receita = receitas.objeto_receita(chave) #cria o objeto
        dici_receita = vars(obj_receita) # transforma em dicionario

        self.receitas[chave] = dici_receita # adiciona o dicionario da receita em um dicionario maior

        self.id_receita = self.id_receita + 1

        print('Receita adicionada com sucesso!')


    def calcular_receitas(self):
        total = 0 
        for receita in self.receitas.values(): #PERCORRE O DICIONARIO DE GASTOS
            for valor in receita.values(): #PERCORRE O DICIONARIO DE APENAS UM GASTO
                if isinstance(valor, (int, float)): #VERIFICA SE O VALOR É UM NUMERO 
                    total += valor #SOMA O VALOR

        return total



    def adicionar_gastos(self):
        chave = self.id_gasto

        obj_gasto = gastos.objeto_gasto(chave)
        dici_gasto = vars(obj_gasto)

        self.gastos[chave] = dici_gasto

        self.id_gasto = self.id_gasto + 1
        print('Gasto adicionado com sucesso!')


    def calcular_gastos(self):
        total = 0 
        for gasto in self.gastos.values(): #PERCORRE O DICIONARIO DE GASTOS
            for valor in gasto.values(): #PERCORRE O DICIONARIO DE APENAS UM GASTO
                if isinstance(valor, (int, float)): #VERIFICA SE O VALOR É UM NUMERO 
                    total += valor #SOMA O VALOR

        return total



    def adicionar_cartoes(self):
        chave = self.id_cartao

        obj_cartao = cartao.objeto_cartao(chave)
        dici_cartao = vars(obj_cartao)

        self.cartoes[chave] = dici_cartao

        self.id_cartao = self.id_cartao + 1
        print('Cartão adicionado com sucesso!')



    def criar_reserva(self):
        chave = reserva.objeto_reserva()
        self.receitas[chave] = {} 

        print('Reserva adicionada com sucesso')


    def exibir_extrato(self):

        print(f"Banco: {self.banco}")
        print(f"Saldo: R$ {self.saldo:.2f}")

        print("\nReceitas")
        for receita in self.receitas.values():
            print(receita)

        print("\nGastos")
        for gasto in self.gasto.values():
            print(gasto)
        
    
    def exibir_saldo(self):
        total_gasto = self.calcular_gastos()
        total_receitas = self.calcular_receitas()
        saldo = total_receitas - total_gasto
        print(f"SALDO: {saldo} ")


    def to_dict(self):
        return {
            "banco": self.banco,
            "apelido": self.apelido,
            "saldo": self.saldo,
            "gastos": [gasto.to_dict() for gasto in self.gastos],
            "receitas": [receita.to_dict() for receita in self.receitas],
            "cartoes": [cartao.to_dict() for cartao in self.cartoes],
            "reservas": [reserva.to_dict() for reserva in self.reservas]

        }

def objeto_conta():
    banco = input('BANCO: ')
    apelido = input('APELIDO: ')
    return contas(banco, apelido)

cont = objeto_conta()