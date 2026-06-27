from datetime import date 
data_atual = date.today() 
print(data_atual)


from datetime import date

class Registro:
    # Variável de classe comum
    data_sistema = date.today() 

# Testando o uso
print(Registro.data_sistema) # Acessa direto pela classe
