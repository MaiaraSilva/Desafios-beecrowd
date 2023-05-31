idade = int(input())  # Lê o valor inteiro correspondente à idade em dias e armazena na variável idade_em_dias

anos = idade // 365  # Calcula a quantidade de anos dividindo idade_em_dias por 365 e armazena em anos
idade %= 365  # Atualiza idade_em_dias com o resto da divisão por 365

meses = idade // 30  # Calcula a quantidade de meses dividindo idade_em_dias por 30 e armazena em meses
idade %= 30  # Atualiza idade_em_dias com o resto da divisão por 30

dias = idade  # Os dias restantes são armazenados em dias

print(f'{anos} ano(s)')  # Imprime a quantidade de anos
print(f'{meses} mes(es)')  # Imprime a quantidade de meses
print(f'{dias} dia(s)')   # Imprime a quantidade de dias