a, b, c  = input().split()
a, b, c = float(a), float(b), float(c)

area_triangulo = (a * c) / 2
area_circulo = c * c * 3.14159
area_trapezio = ((a + b) * c) / 2
area_quadrado = b * b
area_retangulo = a * b

print(f'TRIANGULO: {area_triangulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')