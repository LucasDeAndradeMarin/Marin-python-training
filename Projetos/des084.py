dados = list()
pessoas = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    if len(pessoas) ==0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < maior:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cont = ' '

    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont in 'N':
        break
print('-=-'*30)
print(f'Ao todo, {len(pessoas)} pessoas foram cadastradas. ')
print(f'A maior idade é de {maior} anos de ', end='')
for p in pessoas:
    if p[1] ==maior:
        print(f'{p[0]}', end='')
print()
print(f'A menor idade é de {menor} anos de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end='')