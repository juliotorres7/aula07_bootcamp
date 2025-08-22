import csv

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Funçao que le um arquivo e retorna uma lista de dicionario
    """
    lista = []
    with open(nome_do_arquivo_csv, mode='r',encoding='utf-8') as arquivo:
        
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

def agrupar_categoria(recebe_dados: list[dict]) -> float:
    """
    Calcula o valor por categoria
    """
    grouped_sums = {}

    for item in recebe_dados:
        category = item["Categoria"]
        value = item["Venda"]
        if category in grouped_sums:
            grouped_sums[category] += int(value)
        else:
            grouped_sums[category] = int(value)

    return grouped_sums

