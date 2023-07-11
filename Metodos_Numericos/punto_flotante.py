import tkinter as tk
from tkinter import messagebox

# Frame para conversion a punto flotante


def punto_flotante():

    window1 = tk.Tk()
    window1.geometry("450x450")
    window1.title("Punto Flotante")
    window1.eval('tk::PlaceWindow . center')
    window1.configure(bg='#2b2d31')

    # Titulo
    espacio_titulo = tk.Label(window1, text="\n", anchor='center', bg='#2b2d31')
    espacio_titulo.config(font=('montserrat bold', 2), foreground='white')
    espacio_titulo.pack()

    titulo_label = tk.Label(window1, text="Calculo Punto Flotante", anchor='center', bg='#2b2d31')
    titulo_label.config(font=('montserrat bold', 18), foreground='white')
    titulo_label.pack()

    # Crea los espacios, botones
    number_label = tk.Label(window1, text="Nùmero:")
    number_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
    number_field = tk.Entry(window1)
    bits_label = tk.Label(window1, text="Bits:")
    bits_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
    bits_field = tk.Entry(window1)

    # Convierte el numero dado a bits
    def convertir_a_bits():

        numero = int(number_field.get())
        bits = int(bits_field.get())
        binaryString = bin(numero)[2:]
        #   paddedString = f"{binaryString:0>{bits}}"

        messagebox.showinfo(message="El nùmero convertido a bits es: " + str(binaryString), title="bits")

    convert_button = tk.Button(window1, text="Convertir", bg='#404249', activebackground='#2b2d31', command=convertir_a_bits)
    convert_button.config(width=15, foreground='white', font='bold')

    # Add the widgets to the layout
    number_label.pack(padx=5, pady=5)
    number_field.pack(padx=5, pady=5)
    bits_label.pack(padx=5, pady=5)
    bits_field.pack(padx=5, pady=5)
    convert_button.pack(padx=15, pady=15)

    window1.mainloop()
