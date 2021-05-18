from desafios import desa109
n = float(input('Digite o preço: '))
print(f'A metade de {desa109.moeda(n)} é {desa109.metade(n, True)}')
print(f'O dobro de {desa109.moeda(n)} é {desa109.dobro(n, True)}')
print(f'Aumentando 10%, temos {desa109.aumento(n, 10, True)}')
print(f'Reduzindo 13%, temos {desa109.diminuir(n, 13, True)}')