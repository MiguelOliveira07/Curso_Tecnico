from bs4 import BeautifulSoup
from requests import get

url = 'https://lista.mercadolivre.com.br/_Container_ms-lp_NoIndex_True'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/134.0.0.0 Safari/537.36' 
}

resposta = get(url, headers = headers, verify = False)

sopa = BeautifulSoup(resposta.text,  'html.parser')

eletronicos = sopa.find_all(class_="poly-component__title")
preços = sopa.find_all(class_="andes-money-amount--cents-superscript")


lista_nomes = []
lista_precos = []


for eletronico in eletronicos:
    lista_nomes.append(eletronico.text)
    
for preço in preços:
    lista_precos.append(preço.text)


for i, nome in enumerate(lista_nomes):
        print(f'{nome} --->  \033[42m{lista_precos[i]}\033[0m')