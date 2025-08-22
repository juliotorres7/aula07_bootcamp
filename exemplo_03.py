from typing import List
def contar_valores_unicos(lista: List[int]) -> int:

    if not isinstance(lista, List):
        return "voce não informou uma lista"
    if not all(isinstance(x, int) for x in lista):
        return "Voce informou uma lista, porem não informou valores inteiros"

    return len(set(lista))

teste = contar_valores_unicos([12.1,13.1,14.1])

teste2 = contar_valores_unicos(5)

teste3 = contar_valores_unicos([12,13,14])

print(teste)
print(teste2)
print(teste3)