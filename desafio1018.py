valor = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]
quantidades = []

print(valor)

for nota in notas:
    quantidade = valor // nota
    quantidades.append(quantidade)
    valor %= nota

for i in range(len(notas)):
    print("{} nota(s) de R$ {},00".format(quantidades[i], notas[i]))