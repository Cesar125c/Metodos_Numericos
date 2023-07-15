import tkinter as tk
from tkinter import messagebox


def propagacion():
    window_errores = tk.Tk()
    window_errores.geometry("450x450")
    window_errores.title("Calculo de Errores")
    window_errores.eval('tk::PlaceWindow . center')
    window_errores.configure(bg='#2b2d31')

    # Titulo
    espacio_titulo = tk.Label(window_errores, text="\n", anchor='center', bg='#2b2d31')
    espacio_titulo.config(font=('montserrat bold', 2), foreground='white')
    espacio_titulo.pack()

    titulo_label = tk.Label(window_errores, text="Propagación de Errores", anchor='center', bg='#2b2d31')
    titulo_label.config(font=('montserrat bold', 18), foreground='white')
    titulo_label.pack()

    def calcular_propagacion():
        #   Validar si hay un valor ingresado
        if (valmedido_field.get() == '') | (errorMedido_field.get() == '') | (const_field.get() == ''):
            messagebox.showinfo(message="Por favor ingrese un valor")

        valor_medido = float(valmedido_field.get())
        error_medido = float(errorMedido_field.get())
        cst_propagacion = float(const_field.get())

        error_propagado = abs(cst_propagacion) * error_medido

        messagebox.showinfo(message="Error Propagado: " + str(error_propagado))

    # Crear botones y espacios

    valMedido_label = tk.Label(window_errores, text="Valor Medido:")
    valMedido_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
    valmedido_field = tk.Entry(window_errores)

    errorMedido_label = tk.Label(window_errores, text="Valor Real:")
    errorMedido_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
    errorMedido_field = tk.Entry(window_errores)

    const_label = tk.Label(window_errores, text="Constante de Propagación:")
    const_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
    const_field = tk.Entry(window_errores)

    cal_button = tk.Button(window_errores, text="Calcular", bg='#404249',
                           activebackground='#2b2d31', command=calcular_propagacion)
    cal_button.config(width=15, foreground='white', font='bold')

    # Agregar a pantalla

    valMedido_label.pack(pady=5, padx=5)
    valmedido_field.pack(pady=5, padx=5)

    errorMedido_label.pack(pady=5, padx=5)
    errorMedido_field.pack(pady=5, padx=5)

    const_label.pack(pady=5, padx=5)
    const_field.pack(pady=5, padx=5)

    cal_button.pack(pady=5, padx=5)
