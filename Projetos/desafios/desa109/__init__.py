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