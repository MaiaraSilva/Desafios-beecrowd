valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
quantidades = []

print("NOTAS:")

for nota in notas:
    quantidade = int(valor / nota)
    quantidades.append(quantidade)
    valor -= quantidade * nota
    print("{} nota(s) de R$ {:.2f}".format(quantidade, nota))

print("MOEDAS:")

for moeda in moedas:
    quantidade = int(round(valor, 2) / moeda)
    quantidades.append(quantidade)
    valor = round(valor - quantidade * moeda, 2)
    print("{} moeda(s) de R$ {:.2f}".format(quantidade, moeda))