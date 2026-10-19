from bs4 import BeautifulSoup
from requests import get

url = 'https://lista.mercadolivre.com.br/pe%C3%A7as-para-pc-gamer#D[A:pe%C3%A7as%20para%20pc%20gamer]'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/134.0.0.0 Safari/537.36' 
}

resposta = get(url, headers = headers, verify = False)

sopa = BeautifulSoup(resposta.text,  'html.parser')

peças = sopa.find_all(class_="poly-component__title")
preços = sopa.find_all(class_="andes-money-amount--cents-superscript")

lista_pecas = []
lista_precos = []


for item in peças:
    lista_pecas.append(item.text)
    
for preço in preços:
    lista_precos.append(preço.text)

for i, nome in enumerate(lista_pecas):
        print(f'{nome} --->  \033[42m{lista_precos[i]}\033[0m')