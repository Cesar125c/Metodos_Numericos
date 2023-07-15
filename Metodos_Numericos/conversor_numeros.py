import tkinter as tk
from tkinter import messagebox


# Frame para conversiones Binario-Decimal
def conversor_numeros():
    window2 = tk.Tk()
    window2.geometry("450x450")
    window2.title("Conversor de Nùmeros")
    window2.eval('tk::PlaceWindow . center')
    window2.configure(bg='#2b2d31')

    # Titulo
    espacio_titulo = tk.Label(window2, text="\n", anchor='center', bg='#2b2d31')
    espacio_titulo.config(font=('montserrat bold', 2), foreground='white')
    espacio_titulo.pack()

    titulo_label = tk.Label(window2, text="Conversor Binario-Decimal", anchor='center', bg='#2b2d31')
    titulo_label.config(font=('montserrat bold', 18), foreground='white')
    titulo_label.pack()

    # Este metodo convierte un Binario a Decimal
    def convertir_a_decimal():
        #   Validar si hay un valor ingresado
        if bin_field.get() == '':
            messagebox.showinfo(message="Por favor ingrese un valor")

        binario = int(bin_field.get())

        def bin_a_decimal(binario):
            binario_string = str(binario)
            posicion = 0
            decimal = 0

            binario_string = binario_string[::-1]
            for digito in binario_string:
                # Elevar 2 a la posición actual
                multiplicador = 2 ** posicion
                decimal += int(digito) * multiplicador
                posicion += 1
            return decimal
        messagebox.showinfo(message="El nùmero binario convertido a decimal es: " + str(bin_a_decimal(binario)),
                            title="decimal")

    # Este metodo convierte un Decimal a Binario
    def convertir_a_binario():
        #   Validar si hay un valor ingresado
        if dec_field.get() == '':
            messagebox.showinfo(message="Por favor ingrese un valor")

        decimal = int(dec_field.get())
        if decimal <= 0:
            messagebox.showinfo("0")

        binario = ""
        while decimal > 0:
            # Saber si es 1 o 0
            residuo = int(decimal % 2)
            # E ir dividiendo el decimal
            decimal = int(decimal / 2)
            # Ir agregando el número (1 o 0) a la izquierda del resultado
            binario = str(residuo) + binario
        messagebox.showinfo(message="El nùmero decimal convertido a binario es: " + binario, title="Binario")

    # Crea los botones, espacios
    bin_label = tk.Label(window2, text="Binario:")
    bin_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
    bin_field = tk.Entry(window2)

    bin_button = tk.Button(window2, text="Convertir a Decimal", bg='#404249', activebackground='#2b2d31',
                           command=convertir_a_decimal)
    bin_button.config(width=15, foreground='white', font='bold')

    dec_label = tk.Label(window2, text="Decimal:", pady=10)
    dec_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
    dec_field = tk.Entry(window2)

    dec_button = tk.Button(window2, text="Convertir a Binario", bg='#404249', activebackground='#2b2d31',
                           command=convertir_a_binario)
    dec_button.config(width=15, foreground='white', font='bold')

    # Agrega los widgets
    bin_label.pack(pady=5, padx=5)
    bin_field.pack(pady=5, padx=5)
    bin_button.pack(pady=5, padx=5)

    dec_label.pack(pady=5, padx=5)
    dec_field.pack(pady=5, padx=5)
    dec_button.pack(pady=5, padx=5)
