ficha = dict()
partidas = list()
ficha['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {ficha["Nome"]} jogou? '))
for i in range(1, tot+1):
    partidas.append(int(input(f'    Quantos gols na partida {i}: ')))
ficha['Gols'] = partidas[:]
ficha['Total'] = sum(partidas)
print('-=-'*30)
print(ficha)
print('-=-'*30)
for k, v in ficha.items():
    print(f'O campo {k} tem valor {v}')
print('-=-'*30)
print(f'O jogador {ficha["Nome"]} jogou {len(ficha["Gols"])} partidas. ')
for i, v in enumerate(ficha['Gols']):
    print(f'      => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {ficha["Total"]} gols')