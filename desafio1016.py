distancia = int(input())

velocidade_x = 60 # km/h
velocidade_y = 90 # km/h

# Calcula a velocidade relativa entre os carros
velocidade_relativa = velocidade_y - velocidade_x

# Calcula o tempo necessário para que o carro Y alcance o carro X
tempo = (distancia / velocidade_relativa) * 60

# Exibe o resultado na tela
print(f'{int(tempo)} minutos')