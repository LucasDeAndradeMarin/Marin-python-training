def leiaDinheiro(msg):
    valido = False
    valor = 0
    while not valido:
        din = str(input(msg)).strip().replace(',', '.')
        if din.isalpha() or din == '':
            print(f'\033[0;31mERRO! \"{din}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(din)