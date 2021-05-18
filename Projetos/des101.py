from datetime import date


def voto():
    print('-'*30)
    ano = int(input('Em que ano você nasceu? '))
    idade = date.today().year - ano
    print(f'Com {idade} ano: ', end='')
    if idade >= 18:
        print('VOTO OBRIGATÓRIO!')
    elif 16 < idade < 18 or idade > 65:
        print('VOTO OPCIONAL!')
    else:
        print('NÃO VOTA!')


voto()