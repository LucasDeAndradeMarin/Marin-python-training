def metade(p=0):
    resp = p / 2
    return resp


def dobro(p=0):
    resp = p * 2
    return resp


def aumento(p=0, taxa=0):
    resp = p + (p * taxa / 100)
    return resp


def moeda(p=0, m='R$'):
    return f'{m}{p:.2f}'.replace('.', ',')