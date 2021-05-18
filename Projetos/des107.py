from desafios import desa107
num = float(input('Digite o preço: '))
print(f'A metade de R${num} é {desa107.metade(num)}')
print(f'O dobro de R${num} é {desa107.dobro(num)}')
print(f'Aumentando 10%, temos {desa107.aumento(num, 10)}')