# beecrowd | 1021
# Notas e Moedas

money = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
print("NOTAS:")
for nota in notas:
    quantidade = int(money // nota)
    print(f"{quantidade} nota(s) de R$ {nota:.2f}")
    money = money % nota
print("MOEDAS:")
for moeda in moedas:
    quantidade = int(money // moeda)
    print(f"{quantidade} moeda(s) de R$ {moeda:.2f}")
    money = money % moeda