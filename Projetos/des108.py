from desafios import desa108
n = float(input('Digite o preço: '))
print(f'A metade de {desa108.moeda(n)} é {desa108.moeda(desa108.metade(n))}')
print(f'O dobro de {desa108.moeda(n)} é {desa108.moeda(desa108.dobro(n))}')
print(f'Aumentando 10%, temos {desa108.moeda(desa108.aumento(n, 10))}')