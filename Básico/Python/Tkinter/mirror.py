import tkinter as tk

app = tk.Tk()
app.geometry("300x200")

texto_var = tk.StringVar()

entrada = tk.Entry(app, textvariable=texto_var, font=("Arial", 14))
entrada.pack(pady=20)

label_espelho = tk.Label(app, font=("Arial", 14))
label_espelho.pack()

texto_var.trace_add("write", lambda *args: label_espelho.config(text=texto_var.get()))

app.mainloop()

