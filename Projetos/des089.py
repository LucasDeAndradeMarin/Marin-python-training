ficha = list()
while True:
    nome = str(input(('Nome: ')))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input(('Nota 2: ')))
    nota3 = float(input(('Nota 3: ')))
    media = (nota1 + nota2 + nota3) /3
    ficha.append([nome, [nota1, nota2, nota3], media])
    cont =' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont in 'N':
        break
print('-=-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (Digite 999 para parar): '))
    if opc == 999:
        print('FINALIZANDO')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')