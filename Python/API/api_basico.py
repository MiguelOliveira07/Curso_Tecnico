import requests

cep = input('Digite seu cep:')

url_base = f'https://viacep.com.br/ws/{cep}/json/'

resposta = requests.get(url_base)
# print(resposta.text)

endereco = resposta.json()

print(type(endereco))

