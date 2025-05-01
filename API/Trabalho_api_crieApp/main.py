import streamlit as st
import requests
import json
import random
from translate import Translator
from PIL import Image
import io

# Configuração da página
st.set_page_config(page_title="Mundo em Dados", page_icon="🌍", layout="wide")
st.text('Esse site é programado para te ajudar a esolher seu proximo pais de destino, curta suas férias')

pais = st.text_input('Digit o pais desejado')
url_base = 'https://api.api-ninjas.com/v1/country?name={}'.format(pais)

resposta_base = requests.get(url_base, headers={'X-Api-Key': 'OQ5ar98aOuopjjLystaDvw==ZulkwO88axNRWeOE'})

informção_json = resposta_base.json()

st.text(informção_json)

if resposta_base.status_code == requests.codes.ok:
    print(resposta_base.text)
else:
    print("Error:", resposta_base.status_code, resposta_base.text)