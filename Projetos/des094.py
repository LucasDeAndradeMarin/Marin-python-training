pessoa = dict()
lista = list()
soma = media = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while pessoa['Sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    lista.append(pessoa.copy())
    pessoa.clear()
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while cont not in 'SN':
        print('ERRO! Responda apenas S ou N')
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont in 'N':
        break
media = soma / len(lista)
print('-=-'*30)
print(f'A)  Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B)  A média de idade é de {media:5.2f} anos')
print(f'C)  As mulheres cadastradas foram ', end='')
for p in lista:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}, ', end='')
print()
print(f'D)  Lista das pessoas que estão acima da média: ', end='')
for p in lista:
    if p['Idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print('')
print('<<ENCERRADO>>')