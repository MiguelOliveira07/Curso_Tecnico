from tkinter import *

tela = Tk() 

Label(tela, text='Calculadora - v.1.0').pack(pady=10)

tela.geometry('200x200')
display =  Entry(tela)
display .pack(pady=10)

res = Label(tela, text='Resultado')
res.pack(pady=10)

def calcular():
    expr = display.get()
    
    calculo = eval(expr)
    calculo_text = str(calculo)
    
    res.configure(text=calculo_text)
    
btn_res = Button(tela, text="=", command=calcular)
btn_res.pack(pady=10)


tela.mainloop()
