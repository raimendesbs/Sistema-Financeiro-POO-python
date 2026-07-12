from pprint import pprint


class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    
    def __str__(self):
        return (
            f"Nome: {self.nome}"
            f"idade: {self.idade}"
            f"cidade: {self.cidade}"
        )
    
    def dict(self, obj):
        return {
            'Nome': self.nome,
            'Idade': self.idade,
            'Cidade': self.cidade

        }

    
            



banco = {}
def objeto():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cidade = input("Cidade: ")

    return Pessoa(nome, idade, cidade)

p = objeto()
r = objeto()
b = objeto()

dicip = vars(p)
dicir = vars(r)
dicib = vars(b)


banco["1"] = dicip
banco["2"] = dicir
banco["3"] = dicib

print(banco)

for pessoa in banco.values():
    print(pessoa)

def calcular_idades():

    total = 0 
    for pessoa in banco.values(): #PERCORRE O DICIONARIO DE GASTOS
        for valor in pessoa.values(): #PERCORRE O DICIONARIO DE APENAS UM GASTO
            if isinstance(valor, (int, float)): #VERIFICA SE O VALOR É UM NUMERO 
                    total += valor #SOMA O VALOR
    
    return total

print(calcular_idades())