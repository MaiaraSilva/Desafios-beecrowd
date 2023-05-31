n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
lst = [n1, n2, n3, n4, n5, n6]
positivos = 0

for i in lst:
    if i > 0:
        positivos += 1
print(f'{positivos} valores positivos')
