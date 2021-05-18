from time import sleep
times = ('Internacional', 'São Paulo', 'Atlético-MG', 'Flamengo', 'Palmeiras', 'Grêmio',
         'Fluminense', 'Ceará SC', 'Corinthians', 'Santos', 'Bragantino', 'Athletico-PR',
         'Atlético-GO', 'Vasco da Gama', 'Sport Recife', 'Fortaleza', 'Bahia', 'Goiás',
         'Coritiba', 'Botafogo')
print('-=-'*30)
print(f'Lista de Times do Brasileirão: {times}')
sleep(2)
print('-=-'*30)
print(f'Os 5 primeiros são {times[:5]}')
sleep(2)
print('-=-'*30)
print(f'Os 4 últimos são {times[16:]}')
sleep(2)
print('-=-'*30)
print(f'A tabela em ordem alfabética fica: {sorted(times)}')
sleep(2)
print('-=-'*30)
print(f'O Palmeiras está na {times.index("Palmeiras")}ª posição')