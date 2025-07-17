import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

app = tk.Tk()

style = ttk.Style()
style.configure("Meu_estilo.TLabel", font=("Arial", 20), foreground="white", background="white")
pack_config = {"padx": 10, "pady": 5}

nome_label_static = tk.Label(master=app, text='Nome')
nome_label_static.pack(**pack_config)

nome_var = tk.StringVar()
nome_entry = tk.Entry(master=app, textvariable=nome_var)
nome_entry.pack(**pack_config)

nome_label_dynamic = ttk.Label(master=app, textvariable=nome_var, style='Meu_estilo.TLabel')
nome_label_dynamic.pack(**pack_config)

app.mainloop()
