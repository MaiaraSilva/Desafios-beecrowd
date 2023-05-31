n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
lst = [n1, n2, n3, n4, n5]
pares = 0

for i in lst:
    if i % 2 == 0:
        pares += 1
print(f'{pares} valores pares')