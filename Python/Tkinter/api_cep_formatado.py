import tkinter.messagebox
from customtkinter import *
import tkinter
import requests

set_appearance_mode('dark')
set_default_color_theme('green')

janela = CTk()
janela.title('Busca Endereço')
janela.geometry('300x350')

def consultar_api(cep):
    return requests.get(url=f'https://viacep.com.br/ws/{cep}/json/').json()

def buscar_cep():
    cep = campo_cep.get()
    if len(cep) == 8 and cep.isnumeric():
        endereco = consultar_api(cep=cep)
        if not 'erro' in endereco:
            # print(endereco)
            lb_logradouro.configure(text=endereco['logradouro']) 
            lb_complemento.configure(text=endereco['complemento']) 
            lb_localidade.configure(text=endereco['localidade']) 
            lb_bairro.configure(text=endereco['bairro']) 
            lb_uf.configure(text=endereco['uf']) 
        else: 
          tkinter.messagebox.showinfo('Informamos:', 'CEP não encontrado.')
    else:
        tkinter.messagebox.showerror('Inválido!', 'CEP inválido!')
        
CTkLabel(janela, text='Consultar CEP:', font=('Verdan', 18, 'bold')).pack()

campo_cep = CTkEntry(janela, placeholder_text='Digite o CEP...', width=180, fg_color='white')

botao_consulta = CTkButton(janela, text='Buscar', command=buscar_cep, width=200)
lb_complemento = CTkLabel(janela,text='', font=('Calibri', 14, 'bold'))
lb_localidade = CTkLabel(janela,text='', font=('Calibri', 14, 'bold'))
lb_logradouro = CTkLabel(janela,text='', font=('Calibri', 14, 'bold'))
lb_bairro = CTkLabel(janela,text='', font=('Calibri', 14, 'bold'))
lb_uf = CTkLabel(janela,text='', font=('Calibri', 14, 'bold'))

campo_cep.pack(pady=20)
botao_consulta.pack(pady=5)
lb_logradouro.pack(pady=5)
lb_complemento.pack(pady=5)
lb_localidade.pack(pady=5)
lb_bairro.pack(pady=5)
lb_uf.pack(pady=5)

janela.mainloop()
