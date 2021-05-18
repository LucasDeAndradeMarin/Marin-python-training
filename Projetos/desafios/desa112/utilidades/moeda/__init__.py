def metade(p=0, formato=False):
    resp = p / 2
    return resp if formato is False else moeda(resp)


def dobro(p=0, formato=False):
    resp = p * 2
    return resp if formato is False else moeda(resp)


def aumento(p=0, taxa=0, formato=False):
    resp = p + (p * taxa / 100)
    return resp if formato is False else moeda(resp)


def moeda(p=0, m='R$'):
    return f'{m}{p:.2f}'.replace('.', ',')


def diminuir(p=0, taxa=0, formato=False):
    resp = p - (p * taxa / 100)
    return resp if formato is False else moeda(resp)


def resumo(p=0, au=10, red=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{au}% de aumento: \t{aumento(p, au, True)}')
    print(f'{red}% de redução: \t{diminuir(p, red, True)}')
    print('-'*30)