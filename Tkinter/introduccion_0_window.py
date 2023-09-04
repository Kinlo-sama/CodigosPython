import tkinter as tk 
window = tk.Tk()

label = tk.Label(text="Hola, TKiter",width=30,height=3)
button = tk.Button(text="CLick me!")

button.pack()
label.pack()

window.mainloop()