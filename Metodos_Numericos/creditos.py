import tkinter as tk


def creditos():

    window_creditos = tk.Tk()
    window_creditos.geometry("450x450")
    window_creditos.title("Calculo de Errores")
    window_creditos.eval('tk::PlaceWindow . center')
    window_creditos.configure(bg='#2b2d31')

    # Titulo
    espacio_titulo = tk.Label(window_creditos, text="\n", anchor='center', bg='#2b2d31')
    espacio_titulo.config(font=('montserrat bold', 2), foreground='white')
    espacio_titulo.pack()

    titulo_label = tk.Label(window_creditos, text="Métodos Numéricos", anchor='center', bg='#2b2d31')
    titulo_label.config(font=('montserrat bold', 20), foreground='white')
    titulo_label.pack()

    espacios = tk.Label(window_creditos, text="\n" + "\n" + "\n")
    espacios.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
    espacios.pack()


    # Nombres integrantes
    chicaiza_label = tk.Label(window_creditos, text="Kevin Chicaiza")
    chicaiza_label.config(font=('montserrat bold', 15), foreground='white', bg='#2b2d31')
    chicaiza_label.pack(padx=10, pady=5, ipadx=5, ipady=5)

    cueva_label = tk.Label(window_creditos, text="Cesar Cueva")
    cueva_label.config(font=('montserrat bold', 15), foreground='white', bg='#2b2d31')
    cueva_label.pack(anchor='center', padx=5, pady=5, ipadx=5, ipady=5)

    guerron_label = tk.Label(window_creditos, text="Emily Guerron")
    guerron_label.config(font=('montserrat bold', 15), foreground='white', bg='#2b2d31')
    guerron_label.pack(anchor='center', padx=5, pady=5, ipadx=5, ipady=5)

    muzo_label = tk.Label(window_creditos, text="Alex Muzo")
    muzo_label.config(font=('montserrat bold', 15), foreground='white', bg='#2b2d31')
    muzo_label.pack(anchor='center', padx=5, pady=5, ipadx=5, ipady=5)

    robayo_label = tk.Label(window_creditos, text="Carlos Robayo")
    robayo_label.config(font=('montserrat bold', 15), foreground='white', bg='#2b2d31')
    robayo_label.pack(anchor='center', padx=5, pady=5, ipadx=5, ipady=5)
