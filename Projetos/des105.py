def notas(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        if 5 <= r['Média'] < 7:
            r['Situação'] = 'RAZOÁVEL'
        elif r['Média'] < 5:
            r['Situação'] = 'RUIM'
    return r


resp = notas(4, 4, 5, sit=True)
print(resp)
