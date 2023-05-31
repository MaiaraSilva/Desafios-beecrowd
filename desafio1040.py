n1, n2, n3, n4  = input().split()
n1, n2, n3, n4 = float(n1), float(n2), float(n3), float(n4)

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

if media >= 7:
    print(f'Media: {media:.1f}')
    print("Aluno aprovado.")
elif media < 5:
    print(f'Media: {media:.1f}')
    print("Aluno reprovado.")
elif media < 6.9:
    print(f'Media: {media:.1f}')
    print("Aluno em exame.")
    exame= float(input())
    print(f'Nota do exame: {exame:.1f}')
    recalcular = (exame + media) / 2
    if recalcular >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {recalcular:.1f}")
    else: 
        print("Aluno reprovado.")
        print(f"Media final: {recalcular:.1f}")