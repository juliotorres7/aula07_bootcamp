print("teste")

valor_1 = 4
valor_2 = 6

valor_3 = 50
valor_4 = 30

def soma(valor_1: float,valor_2: float = 10) -> float:
    """
    uma funçao simples de soma do tipo float
    """
    
    valor_3 = valor_1 * valor_2
    return valor_3

valor_33 = soma(valor_1,valor_2)

valor_66 = soma(valor_3,valor_4)

valor_77 = soma(valor_3)

print(valor_33)
print(valor_66)
print(valor_77)