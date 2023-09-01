import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def kutta():
  window_kutta = tk.Tk()
  window_kutta.geometry("450x450")
  window_kutta.title("Runge-Kutta")
  window_kutta.eval('tk::PlaceWindow . center')
  window_kutta.configure(bg='#2b2d31')

  # Titulo
  espacio_titulo = tk.Label(window_kutta, text="\n", anchor='center', bg='#2b2d31')
  espacio_titulo.config(font=('montserrat bold', 2), foreground='white')
  espacio_titulo.pack()

  titulo_label = tk.Label(window_kutta, text="Runge-Kutta", anchor='center', bg='#2b2d31')
  titulo_label.config(font=('montserrat bold', 18), foreground='white')
  titulo_label.pack()



  # Solución de runge-kutta
  def rk4():
    # Obtener los valores
    diff_eq = ecu_field.get()
    f = lambda t, y: eval(diff_eq)
    y0 = float(y_field.get())
    t0 = float(tinicial_field.get())
    t_end = float(tend_field.get())
    h = float(h_field.get())

    t = t0
    y = y0
    t_values = [t]
    y_values = [y]

    while t < t_end:
      k1 = h * f(t, y)
      k2 = h * f(t + h / 2, y + k1 / 2)
      k3 = h * f(t + h / 2, y + k2 / 2)
      k4 = h * f(t + h, y + k3)

      y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
      t = t + h

      t_values.append(t)
      y_values.append(y)

    update_plot(t_values, y_values)

    return t_values, y_values

  # Crea los botones, espacios
  ecu_label = tk.Label(window_kutta, text="Ecuación Diferencial: ")
  ecu_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
  ecu_field = tk.Entry(window_kutta)

  def update_plot(t_values, y_values):
    ax.clear()
    ax.plot(t_values, y_values, marker='o', linestyle='-', color='b')
    ax.set_title('Solución con Método RK4')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Valor de y')
    ax.grid(True)
    canvas.draw()

  # Crear el gráfico de Matplotlib
  fig = Figure(figsize=(6, 4))
  ax = fig.add_subplot(111)

  # Crear el widget Canvas para el gráfico
  canvas = FigureCanvasTkAgg(fig, master=window_kutta)
  canvas_widget = canvas.get_tk_widget()
  canvas_widget.pack()

  tinicial_label = tk.Label(window_kutta, text="Tiempo inicial t(0): ")
  tinicial_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
  tinicial_field = tk.Entry(window_kutta)

  tend_label = tk.Label(window_kutta, text="Tiempo final: ")
  tend_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
  tend_field = tk.Entry(window_kutta)

  y_label = tk.Label(window_kutta, text="Valor inicial y: ")
  y_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
  y_field = tk.Entry(window_kutta)

  h_label = tk.Label(window_kutta, text="Tamaño del paso (h): ")
  h_label.config(font=('montserrat bold', 10), foreground='white', bg='#2b2d31')
  h_field = tk.Entry(window_kutta)

  cal_button = tk.Button(window_kutta, text="Calcular", bg='#404249', activebackground='#2b2d31', command=rk4)
  cal_button.config(width=15, foreground='white', font='bold')

  # Agregar los widgets
  ecu_label.pack(padx=3, pady=3)
  ecu_field.pack(padx=3, pady=3)

  tinicial_label.pack(padx=3, pady=3)
  tinicial_field.pack(padx=3, pady=3)

  tend_label.pack(padx=3, pady=3)
  tend_field.pack(padx=3, pady=3)

  y_label.pack(padx=3, pady=3)
  y_field.pack(padx=3, pady=3)

  h_label.pack(padx=3, pady=3)
  h_field.pack(padx=3, pady=3)

  cal_button.pack(padx=5, pady=5)