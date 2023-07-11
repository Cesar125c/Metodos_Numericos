import tkinter as tk
from tkinter import messagebox


def errores():
    window_errores = tk.Tk()
    window_errores.geometry("450x450")
    window_errores.title("Calculo de Errores")
    window_errores.eval('tk::PlaceWindow . center')
    window_errores.configure(bg='#2b2d31')

    # Titulo
    espacio_titulo = tk.Label(window_errores, text="\n", anchor='center', bg='#2b2d31')
    espacio_titulo.config(font=('montserrat bold', 2), foreground='white')
    espacio_titulo.pack()

    titulo_label = tk.Label(window_errores, text="Calculo de Errores", anchor='center', bg='#2b2d31')
    titulo_label.config(font=('montserrat bold', 18), foreground='white')
    titulo_label.pack()

    def calcular_errores():
        valor_real = float(valr_field.get())
        valor_aproximado = float(valora_field.get())

        error_absoluto = abs(valor_real - valor_aproximado)
        error_relativo = abs(valor_real - valor_aproximado) / abs(valor_real)
        error_porcentual = abs(valor_real - valor_aproximado) / abs(valor_real) * 100

        messagebox.showinfo(message="Error absoluto: " + str(error_absoluto) + "\n" +
                            "Error relativo: " + str(error_relativo) + "\n"+
                            "Error porcentual: " + str(error_porcentual))

    # Crear botones y espacios

    valr_label = tk.Label(window_errores, text="Valor Real:")
    valr_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
    valr_field = tk.Entry(window_errores)

    valora_label = tk.Label(window_errores, text="Valor Aproximado:")
    valora_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
    valora_field = tk.Entry(window_errores)

    calcular_button = tk.Button(window_errores, text="Calcular errores", bg='#404249', activebackground='#2b2d31', command=calcular_errores)
    calcular_button.config(width=15, foreground='white', font='bold')

    # Agregar los widgets

    valr_label.pack(padx=5, pady=5)
    valr_field.pack(padx=5, pady=5)

    valora_label.pack(padx=5, pady=5)
    valora_field.pack(padx=5, pady=5)

    calcular_button.pack(padx=5, pady=5)
