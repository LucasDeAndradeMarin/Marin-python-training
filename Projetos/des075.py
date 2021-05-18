num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
int(input('Digite o último número: ')))
print('Você digitou os números ', end='')
for n in num:
    print(f'{n} ', end='')
print()
print(f'O maior valor, {max(num)}, apareceu {num.count(max(num))} vezes.')
print(f'O menor valor, {min(num)}, apareceu {num.count(min(num))} vezes.')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('Não temos o número 3...')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')