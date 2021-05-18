lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será adicionado!')
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont in 'N':
        break
lista.sort()
print('-=-'*30)
print(f'Você digitou os valores {lista}')
