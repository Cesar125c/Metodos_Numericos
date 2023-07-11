# importar librerias
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import time
import tkinter as tk
from tkinter import ttk
from punto_flotante import punto_flotante
from conversor_numeros import conversor_numeros
from metodo_biseccion import metodo_biseccion
from valores_grandes import valores_grandes
from errores import errores
from creditos import creditos
from propagacion_errores import propagacion


w = Tk()

# Using piece of code from old splash screen
width_of_window = 500
height_of_window = 500
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.eval('tk::PlaceWindow . center')
w.overrideredirect(1)   # for hiding titlebar


def new_win():
    window = tk.Tk()
    window.geometry("450x450")
    window.title("Mètodos Numèricos")
    window.eval('tk::PlaceWindow . center')
    window.configure(bg='#2b2d31')

    # Icono de la aplicacion
    icon = ImageTk.PhotoImage(Image.open('icon.png'))
    window.iconphoto(True, icon)

    # Texto
    titulo = tk.Label(window, text="Métodos Numéricos", anchor="center", bg='#2b2d31')
    titulo.config(font=('montserrat bold', 20), foreground='white')
    # titulo.grid(row=0, column=1, padx=20, pady=10)
    titulo.pack(padx=10, pady=10)

    parrafo_texto = "Programas realizados a lo largo del semestre"
    parrafo = tk.Label(window, text=parrafo_texto, anchor="center", bg='#2b2d31')
    parrafo.config(font=('montserrat bold', 12), foreground='white')
    parrafo.pack(padx=2, pady=2)

    # Crear botones
    boton1 = tk.Button(window, text="Punto Flotante", command=punto_flotante, bg='#404249', activebackground='#2b2d31')
    boton1.config(width=15, foreground='white', font='bold')
    boton1.pack(padx=5, pady=5, ipadx=4, ipady=4)

    boton2 = tk.Button(window, text="Conversor", command=conversor_numeros, bg='#404249', activebackground='#2b2d31')
    boton2.config(width=15, foreground='white', font='bold')
    boton2.pack(padx=5, pady=5, ipadx=4, ipady=4)

    boton3 = tk.Button(window, text="Mètodo de Bisecciòn", command=metodo_biseccion, bg='#404249', activebackground='#2b2d31')
    boton3.config(width=15, foreground='white', font='bold')
    boton3.pack(padx=5, pady=5, ipadx=5, ipady=5)

    boton4 = tk.Button(window, text="Valores Grandes", command=valores_grandes, bg='#404249', activebackground='#2b2d31')
    boton4.config(width=15, foreground='white', font='bold')
    boton4.pack(padx=5, pady=5, ipadx=4, ipady=4)

    boton5 = tk.Button(window, text="Errores", command=errores, bg='#404249', activebackground='#2b2d31')
    boton5.config(width=15, foreground='white', font='bold')
    boton5.pack(padx=5, pady=5, ipadx=4, ipady=4)

    boton6 = tk.Button(window, text="Propagación Errores", command=propagacion, bg='#404249', activebackground='#2b2d31')
    boton6.config(width=15, foreground='white', font='bold')
    boton6.pack(padx=5, pady=5, ipadx=5, ipady=5)

    boton7 = tk.Button(window, text="Créditos", command=creditos, bg='#404249', activebackground='#2b2d31')
    boton7.config(width=15, foreground='white', font='bold')
    boton7.config(width=10)
    boton7.pack(anchor='sw', padx=5, pady=5, ipadx=3, ipady=3)

    window.mainloop()


Frame(w, width=427, height=250, bg='#73171d').place(x=0,y=0)
label1=Label(w, text='METODOS NUMÉRICOS', fg='white', bg='#73171d') #decorate it
label1.configure(font=("Game Of Squids", 24, "bold"))   #You need to install this font in your PC or try another one
label1.place(x=30,y=90)

label2=Label(w, text='Cargando...', fg='white', bg='#73171d') #decorate it
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

# making animation

image_a=ImageTk.PhotoImage(Image.open('Imagenes/c2.png'))
image_b=ImageTk.PhotoImage(Image.open('Imagenes/c1.png'))


for i in range(5): #5loops
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.4)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.4)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.4)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.4)

w.destroy()
new_win()
w.mainloop()
