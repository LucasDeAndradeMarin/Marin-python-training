def coins(x):
    from random import randint
    cara = coroa = 0
    for i in range(0, x):
        resultado = randint(1, 2)
        if resultado == 1:
            cara += 1
        if resultado == 2:
            coroa += 1


    pctgC = cara / x
    pctgCo = coroa / x
    print(f'A porcentagem de vitórias de cara foi de {pctgC*100}%')
    print(f'A porcentagem de vitórias de coroa foi de {pctgCo*100}%')
    if cara > coroa:
        print('\033[30;43m-'*17)
        print('  CARA GANHOU!!')
        print('-'*17)
        print('\033[m')
    elif coroa > cara:
        print('\033[30;46m-'*18)
        print('  COROA GANHOU!!')
        print('-'*18)
        print('\033[m')




print('-'*40)
print('    ESTATÍSTICAS DE COIN FLIPPER')
print('-'*40)
num = int(input('Deseja jogar a moeda quantas vezes? '))
coins(num)






