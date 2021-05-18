lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
        print('Valor adicionado à lista. ')
    elif n > lista[len(lista) - 1]:
        lista.append(n)
        print('Valor adicionado ao final da lista. ')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na {pos}ª posição. ')
                break
            pos += 1
print('-=-'*30)
print(f'Os valores digitados foram {lista} ')