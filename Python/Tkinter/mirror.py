import tkinter as tk
import tkinter.font as tkFont

app = tk.Tk()

tk.Label(master=app, 
    text='Nome',
).pack(
    padx=5,
    pady=5
)

nome_var = tk.StringVar()

nome_entry = tk.Entry(
    master=app,
    textvariable=nome_var
).pack(
    padx=5,
    pady=5
)

nome_label = tk.Label(
    master=app,
    textvariable=nome_var,
    font=('Arial', 20, 'normal')
).pack(
    padx=5,
    pady=5,
    anchor=tk.W
)

app.mainloop()