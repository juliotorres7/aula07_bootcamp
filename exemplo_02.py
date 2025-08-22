def filtrar_acima_de(valores: list[float], limite: float) -> list[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado


teste = filtrar_acima_de([12.1,13.1,14.1], 12.5)

print(teste)