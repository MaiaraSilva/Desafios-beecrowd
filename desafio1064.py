n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
lst = [n1, n2, n3, n4, n5, n6]
positivos = 0
num_positivos = []
soma = 0

for i in lst:
    if i > 0:
        num_positivos.append(i)
        positivos += 1 # verifica a quantidade de numeros positivos
for x in num_positivos:
    soma += x
    media = soma / positivos

print(f'{positivos} valores positivos')
print(f'{media:.1f}')