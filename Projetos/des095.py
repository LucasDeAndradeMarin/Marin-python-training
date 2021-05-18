jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(1, tot+1):
        partidas.append(int(input(f'   Quantos gols na partida {c}: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    partidas.clear()
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while cont not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont in 'N':
        break
print('-=-'*30)
print(' COD ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar Dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    elif busca >= len(time):
        print(f'ERRO! Não existe jogador com tal código! ')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<<<<< VOLTE SEMPRE >>>>>')