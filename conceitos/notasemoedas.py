# beecrowd | 1021
# Notas e Moedas
# Por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

# Saída
# Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

# Obs: Utilize ponto (.) para separar a parte decimal.

# Exemplo de Entrada	Exemplo de Saída
# 576.73

# NOTAS:
# 5 nota(s) de R$ 100.00
# 1 nota(s) de R$ 50.00
# 1 nota(s) de R$ 20.00
# 0 nota(s) de R$ 10.00
# 1 nota(s) de R$ 5.00
# 0 nota(s) de R$ 2.00
# MOEDAS:
# 1 moeda(s) de R$ 1.00
# 1 moeda(s) de R$ 0.50
# 0 moeda(s) de R$ 0.25
# 2 moeda(s) de R$ 0.10
# 0 moeda(s) de R$ 0.05
# 3 moeda(s) de R$ 0.01

# 4.00

# NOTAS:
# 0 nota(s) de R$ 100.00
# 0 nota(s) de R$ 50.00
# 0 nota(s) de R$ 20.00
# 0 nota(s) de R$ 10.00
# 0 nota(s) de R$ 5.00
# 2 nota(s) de R$ 2.00
# MOEDAS:
# 0 moeda(s) de R$ 1.00
# 0 moeda(s) de R$ 0.50
# 0 moeda(s) de R$ 0.25
# 0 moeda(s) de R$ 0.10
# 0 moeda(s) de R$ 0.05
# 0 moeda(s) de R$ 0.01

# 91.01

# NOTAS:
# 0 nota(s) de R$ 100.00
# 1 nota(s) de R$ 50.00
# 2 nota(s) de R$ 20.00
# 0 nota(s) de R$ 10.00
# 0 nota(s) de R$ 5.00
# 0 nota(s) de R$ 2.00
# MOEDAS:
# 1 moeda(s) de R$ 1.00
# 0 moeda(s) de R$ 0.50
# 0 moeda(s) de R$ 0.25
# 0 moeda(s) de R$ 0.10
# 0 moeda(s) de R$ 0.05
# 1 moeda(s) de R$ 0.01

# Solução 1 - Copilot
# valor = float(input())
# notas = [100, 50, 20, 10, 5, 2]
# moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
# print("NOTAS:")
# for nota in notas:
#     quantidade = int(valor // nota)
#     print(f"{quantidade} nota(s) de R$ {nota:.2f}")
#     valor -= quantidade * nota
# print("MOEDAS:")
# for moeda in moedas:
#     quantidade = int(valor // moeda)
#     print(f"{quantidade} moeda(s) de R$ {moeda:.2f}")
#     valor -= quantidade * moeda

# Solução 2 - Manual
# money = float(input())
# notas = [100, 50, 20, 10, 5, 2]
# moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
# print("NOTAS:")
# for nota in notas:
#     quantidade = int(money // nota)
#     print(f"{quantidade} nota(s) de R$ {nota:.2f}")
#     money = money % nota
# print("MOEDAS:")
# for moeda in moedas:
#     quantidade = int(money // moeda)
#     print(f"{quantidade} moeda(s) de R$ {moeda:.2f}")
#     money = money % moeda

# Resultado: Os dois deu erro no final na moeda de 1 centavo(0.01), "pois o valor de money ficou negativo, então a solução é arredondar o valor de money para 2 casas decimais, assim o valor de money não fica negativo e o resultado fica correto."