from customtkinter import *

set_appearance_mode('dark')
set_default_color_theme('green')

app = CTk()

app.geometry('300x300')
app.resizable(False, False)

frame = CTkFrame(app, width=300, height=50, fg_color='blue')
frame.pack()
CTkLabel(frame, text='Calculadora v-2.0', font=('Arial', 20, 'bold'), text_color='white').place(x=50, y=10)

tela = CTkEntry(app, width= 250, font=('Times New Roman', 30, 'bold'))
tela.place(x=26, y=65)

res = CTkLabel(app, width=250, text='Resultado', text_color='Teal', font=('Arial', 25, 'bold'))
res.place(x=25, y=120)

def calcular():
    res.configure(text=str(eval(tela.get())))

btn = CTkButton(app, text='=',font=('Arial', 25, 'bold'), command=calcular)
btn.place(x=79,y=170)

app.mainloop()
