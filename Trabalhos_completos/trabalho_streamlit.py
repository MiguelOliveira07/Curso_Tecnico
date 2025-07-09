import streamlit as st
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
 
st.title('Caçador de Palavras')
 
url = 'https://news.ycombinator.com/'

resposta = requests.get(url, verify=False)
sopa = BeautifulSoup(resposta.text, 'html.parser')
 
texto = sopa.find_all('a')

lista_palavras= []
lista_links = []
word = ''

for a in texto:
    if 'https' in a.get('href'):
        lista_links.append(a.get('href'))
        lista_palavras.append(a.text)
          

for l in lista_palavras:
    word = word + l

wordcloud = WordCloud().generate(word)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()

for link in lista_links:
    st.write(link)
