def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de dimensões {larg}x{comp} é {a}')


print(' CONTROLE DE TERRENOS')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)