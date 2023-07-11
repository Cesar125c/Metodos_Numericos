import tkinter as tk
import math
from tkinter import messagebox


def valores_grandes():
    window4 = tk.Tk()
    window4.geometry("450x450")
    window4.title("Valores Grandes")
    window4.eval('tk::PlaceWindow . center')
    window4.configure(bg='#2b2d31')

    # Titulo
    espacio_titulo = tk.Label(window4, text="\n", anchor='center', bg='#2b2d31')
    espacio_titulo.config(font=('montserrat bold', 2), foreground='white')
    espacio_titulo.pack()

    titulo_label = tk.Label(window4, text="Números > 250", anchor='center', bg='#2b2d31')
    titulo_label.config(font=('montserrat bold', 18), foreground='white')
    titulo_label.pack()

    def calcular_valor():
        x = int(x_field.get())
        x_parte1 = math.exp(x)
        x_parte2 = (math.exp(x)) - 1
        res = x_parte1 / x_parte2

        if x > 250:
            res_field = tk.Label(window4, text="El resultado es 1")
            res_field.pack()
        else:
            x_izq = math.exp(x)
            x_der = (math.exp(x) - 1)

            def truncate(n, decimals=5):
                multiplicar = 10**decimals
                return int(n * multiplicar) / multiplicar
            res = truncate((x_izq / x_der))

            res_field = tk.Label(window4, text="El resultado es: " + str(res))
            res_field.pack()

    # Crear los botones y espacios
    x_label = tk.Label(window4, text=("Ingrese un valor para x > 250"))
    x_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
    x_field = tk.Entry(window4)

    cal_button = tk.Button(window4, text="Calcular", bg='#404249', activebackground='#2b2d31', command=calcular_valor)
    cal_button.config(width=15, foreground='white', font='bold')

    # Agregar los widgets
    x_label.pack(padx=5, pady=5)
    x_field.pack(padx=5, pady=5)
    cal_button.pack(padx=5, pady=5)
