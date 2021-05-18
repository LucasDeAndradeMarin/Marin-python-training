from time import sleep


def maior(* num):
    tot = maior = 0
    print('-=-'*40)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        tot += 1
        if tot == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
    print(f'Foram informador {tot} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()