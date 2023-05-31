salario = float(input())

if salario <= 400:
    ajuste = salario * 0.15
    novo_salario = salario + ajuste
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {ajuste:.2f}')
    print('Em percentual: 15 %')
elif salario <= 800:
    ajuste = salario * 0.12
    novo_salario = salario + ajuste
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {ajuste:.2f}')
    print('Em percentual: 12 %')
elif salario <= 1200:
    ajuste = salario * 0.10
    novo_salario = salario + ajuste
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {ajuste:.2f}')
    print('Em percentual: 10 %')
elif salario <= 2000:
    ajuste = salario * 0.07
    novo_salario = salario + ajuste
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {ajuste:.2f}')
    print('Em percentual: 7 %')
elif salario >= 2000:
    ajuste = salario * 0.04
    novo_salario = salario + ajuste
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {ajuste:.2f}')
    print('Em percentual: 4 %')