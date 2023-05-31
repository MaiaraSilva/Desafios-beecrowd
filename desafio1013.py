a, b, c  = input().split()
a, b, c = int(a), int(b), int(c)

maiorab = (a + b + abs(a - b)) // 2

maiorc = (maiorab + c + abs(maiorab - c)) // 2

resultado = maiorc

print(f'{resultado} eh o maior')