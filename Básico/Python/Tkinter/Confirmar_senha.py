import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

app = tk.Tk()
app.geometry('250x300')
app.resizable(False, False)

# label_style_config = { "font":("Amargo", 16, "normal"), "foreground":"white",}
# entry_style_config = {"font": ("Arial", 16),"width": 40,"show": "*"}
pack_config = {"padx": 20, "pady": 10}

entry_style_config = {"font": ("Arial", 16),"width": 40,"show": "*","relief": "solid","bd": 2}

button_style_config = {"font": ("Arial", 14, "bold"),"activebackground": "darkgray","relief": "raised","bd": 3}

label_style_config = {"font": ("Arial", 12, "normal"),}

def Verificar_senhas():
    if not Entry_senha_nova.get() or not Entry_confirmar_senha.get():
        Resultado_label.configure(text='Campo vazio!')
        app.configure(background='gray')
    elif ( Entry_senha_nova.get() != Entry_confirmar_senha.get()):
        Resultado_label.configure(text='Senhas não compatíveis!')               
        app.configure(background='red')
    else:
        Resultado_label.configure(text='Confirmado!')
        app.configure(background='green')

Senha_nova_label = tk.Label(master=app, text='Insira Nova Senha:', **label_style_config)
Senha_nova_label.pack(**pack_config)

nome_var = tk.StringVar()
Entry_senha_nova = tk.Entry(master=app, **entry_style_config)
Entry_senha_nova.pack(**pack_config)

Senha_confirmar_label = tk.Label(master=app, text='Confirme a Senha:', **label_style_config)
Senha_confirmar_label.pack(**pack_config)

Entry_confirmar_senha = tk.Entry(master=app, **entry_style_config)
Entry_confirmar_senha.pack(**pack_config)

Resultado_label = tk.Label(master=app, text='Resultado', **label_style_config)
Resultado_label.pack(**pack_config)


btn_confirmar = tk.Button(master=app, text='Confirme',**button_style_config, command=Verificar_senhas)
btn_confirmar.pack(**pack_config)

# nome_var = tk.StringVar()
# nome_label_dynamic = ttk.Label(master=app, textvariable=nome_var, style='Meu_estilo.TLabel')
# nome_label_dynamic.pack(**pack_config)

app.mainloop()
