import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para generar y mostrar la señal senoidal
def generar_senoidal():
    amplitud = float(amplitud_entry.get())
    tiempo = float(tiempo_entry.get())
    frecuencia_angular = float(frecuencia_angular_entry.get())
    desfase_angular = float(desfase_angular_entry.get())

    tiempo_muestreo = 0.001  # Intervalo de muestreo
    tiempo_muestreo_vals = np.arange(0, tiempo, tiempo_muestreo)
    if seno_coseno_var.get() == "Seno":
        seno_vals = amplitud * np.sin(frecuencia_angular * tiempo_muestreo_vals + desfase_angular)
    else:
        seno_vals = amplitud * np.cos(frecuencia_angular * tiempo_muestreo_vals + desfase_angular)

    plt.figure(figsize=(6, 4))
    plt.plot(tiempo_muestreo_vals, seno_vals)
    plt.title("Señal Senoidal")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    # Mostrar la señal en la interfaz gráfica
    canvas = FigureCanvasTkAgg(plt.gcf(), master=ventana)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=7, columnspan=2)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Señales Senoidales")

# Crear etiquetas y campos de entrada
amplitud_label = ttk.Label(ventana, text="Amplitud:")
amplitud_label.grid(row=0, column=0)
amplitud_entry = ttk.Entry(ventana)
amplitud_entry.grid(row=0, column=1)

tiempo_label = ttk.Label(ventana, text="Tiempo (s):")
tiempo_label.grid(row=1, column=0)
tiempo_entry = ttk.Entry(ventana)
tiempo_entry.grid(row=1, column=1)

frecuencia_angular_label = ttk.Label(ventana, text="Frecuencia Angular (rad/s):")
frecuencia_angular_label.grid(row=2, column=0)
frecuencia_angular_entry = ttk.Entry(ventana)
frecuencia_angular_entry.grid(row=2, column=1)

desfase_angular_label = ttk.Label(ventana, text="Desfase Angular (radianes):")
desfase_angular_label.grid(row=3, column=0)
desfase_angular_entry = ttk.Entry(ventana)
desfase_angular_entry.grid(row=3, column=1)

seno_coseno_label = ttk.Label(ventana, text="Tipo de Señal:")
seno_coseno_label.grid(row=4, column=0)
seno_coseno_var = tk.StringVar()
seno_coseno_combobox = ttk.Combobox(ventana, textvariable=seno_coseno_var, values=["Seno", "Coseno"])
seno_coseno_combobox.grid(row=4, column=1)
seno_coseno_combobox.set("Seno")

# Botón para generar la señal
generar_boton = ttk.Button(ventana, text="Generar Señal", command=generar_senoidal)
generar_boton.grid(row=5, columnspan=2)

# Iniciar la interfaz gráfica
ventana.mainloop()