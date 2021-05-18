matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
princ = (matriz[0][0]*matriz[1][1]*matriz[2][2]) + (matriz[0][1]*matriz[1][2]*matriz[2][0]) + (matriz[0][2]*matriz[1][0]*matriz[2][1])
sec = (matriz[2][0]*matriz[1][1]*matriz[0][2]) + (matriz[2][1]*matriz[1][2]*matriz[0][0]) + (matriz[2][2]*matriz[1][0]*matriz[0][1])
det = princ - sec
print('-=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=-'*25)
print(f'Como a diagonal principal equivale à {princ} e a secundária à {sec}, o determinante equivale à: {det}')