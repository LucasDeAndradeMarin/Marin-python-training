lista = list()
maior = menor = 0
for num in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {num}: ')))
    if num == 0:
        maior = menor = lista[num]
    else:
        if lista[num] > maior:
            maior = lista[num]
        if lista[num] < menor:
            menor = lista[num]
print('-=-'*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()