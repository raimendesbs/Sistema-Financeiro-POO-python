from datetime import date 


class cartao:
    data_atual = date.today()
    def __init__(self, id, nome='', limite=0, vencimento=data_atual):
        self.id = id
        self.nome = nome
        self.limite = limite
        self.vencimento = vencimento

        self.gastos = []


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