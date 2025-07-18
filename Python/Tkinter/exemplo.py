import tkinter as tk

def mudou_valor(*args):
    print('O valor mudou para', var.get())
    
app = tk.Tk()


var = tk.StringVar()
var.trace_add('write', mudou_valor)

label = tk.Label(app, text='Senha')
label.pack()

campo = tk.Entry(master=app, textvariable=var)
campo.pack()

app.mainloop()