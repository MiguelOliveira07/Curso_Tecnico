import streamlit as st
import requests

# --- FUNÇÕES ---

# Buscar ID do país pela API do IBGE
def buscar_id_pais(pais_nome):
    url = "https://servicodados.ibge.gov.br/api/v1/paises"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        return None

    pais_nome = pais_nome.strip().lower()

    for pais in resposta.json():
        nome_abreviado = pais.get('nome', {}).get('abreviado', '').lower()
        iso = pais.get('id', {}).get('ISO-ALPHA-3')

        if pais_nome in nome_abreviado or nome_abreviado in pais_nome:
            return iso

    return None

# Buscar ID do indicador (em português ou inglês)
def buscar_id_indicador_por_nome(nome_indicador):
    url = "https://servicodados.ibge.gov.br/api/v1/paises/indicadores"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        return None

    indicadores = resposta.json()
    nome_indicador = nome_indicador.strip().lower()

    for indicador in indicadores:
        nome_bruto = indicador.get('nome', {})
        nome_pt = nome_bruto.get('pt', '').lower()
        nome_en = nome_bruto.get('en', '').lower()

        if nome_indicador in nome_pt or nome_indicador in nome_en:
            return indicador['id']

    return None

# Buscar dados combinando país e indicador
def buscar_dados_ibge(pais_nome, nome_indicador):
    pais_id = buscar_id_pais(pais_nome)
    indicador_id = buscar_id_indicador_por_nome(nome_indicador)

    if not pais_id:
        return None, "❌ País não encontrado."
    if not indicador_id:
        return None, "❌ Indicador não encontrado."

    url = f"https://servicodados.ibge.gov.br/api/v1/paises/{pais_id}/indicadores/{indicador_id}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json(), None
    else:
        return None, "❌ Erro ao buscar dados do IBGE."

# Buscar bandeira do país usando restcountries
def buscar_bandeira(pais_nome):
    try:
        pais_nome = pais_nome.strip().capitalize()

        # Primeira tentativa: busca exata
        url = f"https://restcountries.com/v3.1/name/{pais_nome}?fullText=true"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            data = resposta.json()
            return data[0]['flags']['png']

        # Segunda tentativa: busca parcial
        url = f"https://restcountries.com/v3.1/name/{pais_nome}"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            data = resposta.json()
            return data[0]['flags']['png']

    except Exception as e:
        print("Erro ao buscar bandeira:", e)

    return None

# --- INTERFACE STREAMLIT ---
st.set_page_config(page_title="Informações sobre Países", layout="centered")
st.title("🌍 Informações sobre Países via IBGE")

idioma = st.radio("Escolha o idioma:", ["Português", "Inglês"])
pais_input = st.text_input("Digite o nome do país:", value="Brasil")
indicador_input = st.text_input("Digite o nome do indicador (ex: população, expectativa de vida):", value="população")

if st.button("🔎 Buscar"):
    if pais_input and indicador_input:
        dados, erro = buscar_dados_ibge(pais_input, indicador_input)
        bandeira_url = buscar_bandeira(pais_input)

        if erro:
            st.error(erro)
        else:
            if bandeira_url:
                st.image(bandeira_url, width=200, caption=f"Bandeira de {pais_input.capitalize()}")

            st.subheader("📊 Resultado:")
            for item in dados[0]['serie']:
                valor = dados[0]['serie'][item]
                if idioma == "Português":
                    st.write(f"Ano: {item} — Valor: {valor}")
                else:
                    st.write(f"Year: {item} — Value: {valor}")
    else:
        st.warning("⚠️ Preencha todos os campos antes de buscar.")
