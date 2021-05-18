def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário decidiu parar agora.........\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário decidiu parar agora .........\033[m')
            return 0
        else:
            return n


inteiro = leiaInt('Digite um número Inteiro: ')
real = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o valor real foi {real}')