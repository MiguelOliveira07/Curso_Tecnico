import tkinter as tk

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

app.mainloop()