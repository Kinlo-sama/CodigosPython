# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 22:19:18 2024

@author: Kinlo
"""

    
import tkinter as tk
from PIL import Image, ImageTk
import random 

def LavarQ1():
    vibrar()

def vibrar():
    # Cambiar la posición de la imagen ligeramente en direcciones aleatorias
    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    canvas.move(imagen_id, dx, dy)
    
    # Programar la función para que se llame de nuevo después de 50 milisegundos
    ventana.after(50, vibrar)
    

# Crear una ventana
ventana = tk.Tk()
ventana.title("Mostrar Imagen")
ventana.geometry("700x600")  # Cambia el tamaño de la ventana

# Crear un lienzo
canvas = tk.Canvas(ventana, width=600, height=450)  # Ajusta el tamaño del lienzo al de la ventana
canvas.pack()
# Cargar la imagen
imagen = Image.open("./Estado1.jpg")
imagen_tk = ImageTk.PhotoImage(imagen)


# Mostrar la imagen en el lienzo
imagen_id = canvas.create_image(300, 225, image=imagen_tk)  # Centra la imagen en el lienzo

# Crear un widget de etiqueta para mostrar la imagen
etiqueta = tk.Label(ventana, image=imagen_tk)

estado1 = tk.Button(ventana, text="Lavar", command=LavarQ1)
estado1.pack()

# Ejecutar el bucle principal
ventana.mainloop()

