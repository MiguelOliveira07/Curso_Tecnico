from customtkinter import *
import requests

janela = CTk()
janela.geometry('300x300')

def consultar_api(cep):
    return requests.get(url=f'https://viacep.com.br/ws/{cep}/json/').json()

def buscar_cep():
    cep = campo_cep.get()
    endereco = consultar_api(cep=cep)
    print(endereco)
    campo_endereco.configure(text=endereco['logradouro'])

CTkLabel(janela, text='Busca Endereço').pack()

campo_cep = CTkEntry(janela)
campo_cep.pack(pady=20)

botao_consulta = CTkButton(janela, text='BUSCAR', command=buscar_cep)
botao_consulta.pack(pady=20)

campo_endereco = CTkLabel(janela, text='Endereço', font=('Arial', 25, 'bold'))
campo_endereco.pack(pady=20)

janela.mainloop()
