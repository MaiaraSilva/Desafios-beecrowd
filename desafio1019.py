# leitura do valor em segundos
segundos = int(input())

# cálculo das horas, minutos e segundos
horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

# exibição do resultado no formato horas:minutos:segundos
print(f"{horas}:{minutos}:{segundos}")