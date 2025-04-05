from bs4 import BeautifulSoup
from requests import get

url = 'https://www.usepronta.com.br/produtos?page=1'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/134.0.0.0 Safari/537.36' 
}

resposta = get(url, headers = headers, verify = False)

sopa = BeautifulSoup(resposta.text,  'html.parser')

nomes = sopa.find_all(class_="product-title")
precos = sopa.find_all(class_="price total")

lista_nomes = []
lista_precos = []


for item in nomes:
    lista_nomes.append(item.text.split())
    
for preço in precos:
    lista_precos.append(preço.text.split())

for i, nome in enumerate(lista_nomes):
        print(f'{" ".join(nome)} --->  \033[42m{" ".join(lista_precos[i])}\033[0m')