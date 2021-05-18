import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mDeu ruim irmão...\033[m')
else:
    print('\033[32mTudo Ok no seu site mestre!\033[m')
