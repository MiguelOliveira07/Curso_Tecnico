from customtkinter import *
import requests

set_appearance_mode('dark')

janela = CTk()
janela.geometry('300x300')
janela.resizable(False, False)

def pesquisar(pais):
    api_url = f'https://api.api-ninjas.com/v1/interestrate?country={pais}'
    response = requests.get(api_url, headers={'X-Api-Key': 'Api-Key'})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return None

def gerar_pesquisa():  
    pais = get_pais.get()
    endereco = pesquisar(pais=pais)
    if endereco:
        resultado = f"{endereco.get('central_bank', '')}, {endereco.get('country', '')}, {endereco.get('rate_pct', '')}% - Última atualização: {endereco.get('last_update', '')}"
    else:
        resultado = "Erro ao obter dados. Verifique o nome do país ou a chave da API."
    res.configure(text=resultado)

CTkLabel(janela, text='Verifique Juros: ', font=('Arial', 20, 'bold'), text_color='#fff', width=250).place(x=25, y=15)

get_pais = CTkEntry(janela, width=250, height=30, fg_color='white', text_color='black')
get_pais.place(x=25, y=50)

btn = CTkButton(janela, text='Consultar', width=150, command=gerar_pesquisa)
btn.place(x=77, y=100)

res = CTkLabel(janela, text='RESULTADO', width=250, height=90, fg_color='white', text_color='black', wraplength=250, justify='left')
res.place(x=25, y=135)

janela.mainloop()
