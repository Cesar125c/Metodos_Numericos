import tkinter as tk
import matplotlib.pyplot as plt # Instalar matplotlib
import numpy as np  # Instalar numpy
from sympy import symbols   # Instalar simpy
from sympy import lambdify
from sympy import sympify
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def metodo_biseccion():
    window3 = tk.Tk()
    window3.geometry("450x450")
    window3.title("Mètodo de Bisecciòn")
    window3.eval('tk::PlaceWindow . center')
    window3.configure(bg='#2b2d31')

    # Titulo
    espacio_titulo = tk.Label(window3, text="\n", anchor='center', bg='#2b2d31')
    espacio_titulo.config(font=('montserrat bold', 2), foreground='white')
    espacio_titulo.pack()

    titulo_label = tk.Label(window3, text="Método de Bisección", anchor='center', bg='#2b2d31')
    titulo_label.config(font=('montserrat bold', 18), foreground='white')
    titulo_label.pack()

    def calcular_raices():

        # Funcion que grafica a partir de los parametros calculados
        def canvas_grafico():
            # Create a canvas display for the plot
            canvas = FigureCanvasTkAgg(fig, master=grafico_frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

            # crear label para resultado
            res_label = tk.Label(grafico_frame, text=("El valor de x es", round(xr, 9), "con un error de", round(ea * 100, 9), "%"))
            res_label.pack()

        # Crear el frame para el grafico
        grafico_frame = tk.Tk()
        grafico_frame.title("Gràfico de la funciòn")

        # Crear un objeto subplot
        fig = plt.figure(figsize=(6, 4), dpi=80)
        ax = fig.add_subplot(111)

        x = symbols('x')    # X es una variable simbolica que se usa en la funcion
        fn = sympify(fun_field.get())   # Definir quien es la funcion
        f = lambdify(x, fn)

        # Definir variables

        a = float(a_field.get())    # Ingresar un valor inicial
        b = float(b_field.get())    # Ingresar un valor inicial
        crit = float(tol_field.get())   # Ingresar criterio de tolerancia
        i = 0   # Iniciar contador
        ea = 1  # Iniciar variable de error
        x_anterior = 0  # Iniciar variable de x anterior

        # Criterio inicial para verificar solucion en intervalo seleccionado
        if f(a) * f(b) < 0:

            while ea > crit:
                xr = (a + b) / 2
                ea = abs((xr - x_anterior) / xr)

                if f(xr) * f(a) < 0:
                    b = xr
                else:
                    a = xr

                x_anterior = xr

                i = i + 1

            # Grafico

            xpts = np.linspace(-10, 10)
            ypts = f(xpts)
            ax.plot(xpts, ypts)

            # Plot the graphic
            ax.set_title("Grafica de la funcion")
            ax.axhline(color="black")
            ax.axvline(color="black")
            ax.scatter(xr, 0, c="red")
            ax.annotate(round(xr, 9), xy=(xr, 0.5))
            ax.set_xlabel("x")
            ax.set_ylabel("f(x)")
            ax.grid(True, which='both')
            ax.set_ylim([-15, 15])

            canvas_grafico()

        else:
            mensaje1 = tk.Label(grafico_frame, text=("La funcion no tiene raiz en el intervalo de " + "x = " +str(a) + " a x = " +str(b)))
            mensaje1.pack()

            try:
                xpts = np.linspace(-10, 10)
                ypts = f(xpts)
                ax.plot(xpts, ypts)

                # Plot the graphic
                ax.set_title("Grafica de la funcion")
                ax.axhline(color="black")
                ax.axvline(color="black")
                ax.set_xlabel("x")
                ax.set_ylabel("f(x)")
                ax.grid(True, which='both')
                ax.set_ylim([-15, 15])

                canvas_grafico()
            except:
                expection_label = tk.Label(grafico_frame, text="Vuelva a ingresar valores en el rango correcto")

    # Crea los botones, espacios
    fun_label = tk.Label(window3, text="Funciòn: ")
    fun_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
    fun_field = tk.Entry(window3)

    a_label = tk.Label(window3, text="Valor inicial a: ")
    a_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
    a_field = tk.Entry(window3)

    b_label = tk.Label(window3, text="Valor inicial b: ")
    b_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
    b_field = tk.Entry(window3)

    tol_label = tk.Label(window3, text="Tolerancia: ")
    tol_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
    tol_field = tk.Entry(window3)

    cal_button = tk.Button(window3, text="Calcular", bg='#404249', activebackground='#2b2d31', command=calcular_raices)
    cal_button.config(width=15, foreground='white', font='bold')

    # Agregar los widgets
    fun_label.pack(padx=3, pady=3)
    fun_field.pack(padx=3, pady=3)

    a_label.pack(padx=3, pady=3)
    a_field.pack(padx=3, pady=3)

    b_label.pack(padx=3, pady=3)
    b_field.pack(padx=3, pady=3)

    tol_label.pack(padx=3, pady=3)
    tol_field.pack(padx=3, pady=3)

    cal_button.pack(padx=5, pady=5)







