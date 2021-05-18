from desafios.desa112.utilidades import moeda
from desafios.desa112.utilidades import dado
p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)