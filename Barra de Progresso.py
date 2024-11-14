from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title("Progress Bar")
root.geometry("500x400")
root.config(bg="#f4f4f4")

def step():
    for x in range(10):
        progress1['value'] += 10
        root.update_idletasks()
        time.sleep(1)

def stop():
    progress1.stop()

# Estilo da barra de progresso
style = ttk.Style()
style.configure("TProgressbar",
                thickness=30,
                font=("Helvetica", 10),
                background="#4CAF50",
                )

progress1 = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate', style="TProgressbar")
progress1.pack(pady=30)

# Estilo dos botões
botao_style = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Helvetica', 12, 'bold'), 'relief': 'flat'}
botao2_style = {'bg': '#f44336', 'fg': 'white', 'font': ('Helvetica', 12, 'bold'), 'relief': 'flat'}

# Botão de progresso
botao = Button(root, text="Progresso", command=step, **botao_style)
botao.pack(pady=10)

# Botão de parar
botao2 = Button(root, text="Parar", command=stop, **botao2_style)
botao2.pack(pady=10)

root.mainloop()
