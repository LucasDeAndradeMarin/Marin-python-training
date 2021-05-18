from time import sleep
c = ('\033[m', '\033[0;30;41m', '\033[1;43m', '\033[1;44m', '\033[7;40m')


def ajuda(com):
    tit(f'Acessando o manual do comando \'{com}\'', 3)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(2)



def tit(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    tit('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
tit('ATÉ LOGO!', 1)