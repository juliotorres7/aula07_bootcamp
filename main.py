
from etl import ler_csv, agrupar_categoria


teste = ler_csv("vendas.csv")

print(teste)

teste2 = agrupar_categoria(teste)

print(teste2)