n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
lst = [n1, n2, n3, n4, n5]
pares = 0
impares = 0
positivo = 0 
negativo = 0

for i in lst:
    if i > 0:
        positivo += 1
    elif i < 0:
        negativo +=1
    
    if i % 2 == 0:
        pares += 1
    elif i % 2 != 0:
        impares += 1
print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')