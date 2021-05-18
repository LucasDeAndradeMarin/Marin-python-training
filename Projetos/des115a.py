from desafios.desa115 import *
from desafios.desa115.arquivo import *
from time import sleep

arq = 'LucasDeAndradeMarin.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Criar Arquivo', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cab('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta ==3:
        cab('    \033[1;36mSaindo do Sistema\033[m')
        break
    else:
        print('\033[31mERRO! DIgite uma opção válida.\033[m')
    sleep(2)

