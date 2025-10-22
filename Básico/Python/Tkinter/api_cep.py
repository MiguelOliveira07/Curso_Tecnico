from customtkinter import *
import requests

set_appearance_mode('dark')

janela = CTk()
janela.geometry('300x300')
janela.resizable(False, False)

def consultarAPI(cep):
    return requests.get(url=f'https://viacep.com.br/ws/{cep}/json/').json()

def buscarCEP():
    cep = sh_cep.get()
    endereco = consultarAPI(cep=cep)
    resultado = f"{endereco.get('logradouro', '')}, {endereco.get('bairro', '')}, {endereco.get('localidade', '')} - {endereco.get('uf', '')}"
    res.configure(text=resultado)

CTkLabel(janela, text='Consulte o CEP:', font=('Arial', 20, 'bold'), text_color='white', width=250).place(x=25, y=15)

sh_cep = CTkEntry(janela, width=250, height=30, fg_color='white', text_color='black')
sh_cep.place(x=25, y=50)

btn = CTkButton(janela, text='Consultar', width=150, command=buscarCEP)
btn.place(x=77, y=100)

res = CTkLabel(janela, text='RESULTADO', width=250, height=90, fg_color='white', text_color='black', wraplength=250, justify='left')
res.place(x=25, y=135)

janela.mainloop()
