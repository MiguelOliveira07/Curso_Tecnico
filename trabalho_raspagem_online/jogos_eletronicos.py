from bs4 import BeautifulSoup
from requests import get

url = 'https://lista.mercadolivre.com.br/jogos-eletronicos#D[A:jogos%20eletronicos]'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/134.0.0.0 Safari/537.36' 
}

resposta = get(url, headers = headers, verify = False)

sopa = BeautifulSoup(resposta.text,  'html.parser')

nome = sopa.find_all(class_="poly-component__title")
preços = sopa.find_all(class_="andes-money-amount--cents-superscript")

lista_nomes = []
lista_precos = []


for item in nome:
    lista_nomes.append(item.text)
    
for preço in preços:
    lista_precos.append(preço.text)

for i, nome in enumerate(lista_nomes):
        print(f'{nome} --->  \033[42m{lista_precos[i]}\033[0m')