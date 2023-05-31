codigo_peca_1, num_peca_1, valor_unitario_1 = input().split()
codigo_peca_1, num_peca_1, valor_unitario_1 = int(codigo_peca_1), int(num_peca_1), float(valor_unitario_1)

codigo_peca_2, num_peca_2, valor_unitario_2 = input().split()
codigo_peca_2, num_peca_2, valor_unitario_2 = int(codigo_peca_2), int(num_peca_2), float(valor_unitario_2)

valor = (num_peca_1* valor_unitario_1) + (num_peca_2 * valor_unitario_2)

print(f'VALOR A PAGAR: R$ {valor:.2f}')