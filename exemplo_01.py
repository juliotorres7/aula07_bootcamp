from typing import List

def calcalar_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

teste = calcalar_media([12.1,13.1,14.1])

print(teste)