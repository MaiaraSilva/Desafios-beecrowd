import math

hora_inicial, hora_final = input().split()
hora_inicial, hora_final= int(hora_inicial), int(hora_final)

if hora_inicial and hora_final == 0:
    print('O JOGO DUROU 1 HORA(S)')
elif hora_inicial < 10 and hora_final >= 10:
    total = abs(hora_inicial - hora_final)
    print(f'O JOGO DUROU {total} HORA(S)')
else:
    total = 24 - hora_inicial + hora_final
    print(f'O JOGO DUROU {total} HORA(S)')