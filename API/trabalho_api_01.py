import requests
from datetime import datetime
import streamlit as st

st.title('Descubra o clima de sua cidade')
st.markdown('---')

# Pega o nome da cidade
cidade = st.text_input('Digite sua cidade:')

if cidade:  # Só executa se o usuário digitou algo
    try:
        # Obtém o código da cidade
        url_cidade = f'https://brasilapi.com.br/api/cptec/v1/cidade/{cidade}' 
        resposta = requests.get(url_cidade)
        city_code = resposta.json()
        id = city_code[0]['id']

        # Obtém a previsão do tempo
        url_clima = f'https://brasilapi.com.br/api/cptec/v1/clima/previsao/{id}'
        resposta_id = requests.get(url_clima)     
        city_weather = resposta_id.json()
        clima_cidade = city_weather['clima']

        # Processa os dados
        descricao = clima_cidade[0]['condicao_desc']
        data = datetime.strptime(clima_cidade[0]['data'], "%Y-%m-%d")
        data_ = data.strftime("%d/%m/%Y")
        min_temp = clima_cidade[0]['min']
        max_temp = clima_cidade[0]['max']

        # Exibe os resultados
        st.markdown('---')
        st.subheader(f'Previsão do tempo para {cidade}')
        st.write(f'**Data:** {data_}')
        st.write(f'**Condição:** {descricao}')
        st.write(f'**Temperatura mínima:** {min_temp}°C')
        st.write(f'**Temperatura máxima:** {max_temp}°C')
        st.markdown('---')

    except Exception as e:
        st.error('Ocorreu um erro ao buscar a previsão do tempo. Verifique o nome da cidade para tentar de novo.')
        st.error(f'Detalhes do erro: {str(e)}')