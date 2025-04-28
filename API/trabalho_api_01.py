import requests
from datetime import datetime

print('==='*20)
print('Descrubra o clima de sua cidade')
print('==='*20)

# Pega o nome da cidade
cidade = input(str('Digite sua cidade : ')) 

# Usa o nome da cidade como parametro para o link de pesquisa da ID
url_cidade = f'https://brasilapi.com.br/api/cptec/v1/cidade/{cidade}' 
 # Faz a requisição HTTP do nosos link
resposta = requests.get(url_cidade)

# Pega o resultado Json da página desse link (dicionário)
city_code = resposta.json()

# # A partir do dicionário pega a inforamção que precisamos para pegar o tempo da cidade [ seu ID ]
id = city_code[0]['id'] 

# # O ID está sendo usado para pegar o clima da cidade, essa cidade corresponde ao ID
url_clima = f'https://brasilapi.com.br/api/cptec/v1/clima/previsao/{id}' 

# # Mesmo processo de pegar as informações
resposta_id = requests.get(url_clima)     
city_weather = resposta_id.json()
clima_cidade = city_weather['clima']

# # Separa as informações que realmente queremos e as torna variaveis
descricao = clima_cidade[0]['condicao_desc']
data = datetime.strptime(clima_cidade[0]['data'],"%Y-%m-%d")
data_ = data.strftime("%d/%m/%Y")
min = clima_cidade[0]['min']
max = clima_cidade[0]['max']

# Apresentaçãop formatada
print(f'\nA data atual é: {data_}')
print(f'\nA descrição é: {descricao}')
print(f'\nA temperatura mínima é : {min}°C')
print(f'\nA temperatura máxima é : {max}°C')
print('==='*20)

