import tkinter as tk
window = tk.Tk()
window.columnconfigure(0,minsize=250)#configura cuantas columas [1] y tamaño 250px
window.rowconfigure([0,1],minsize=100)#configura cuantas filas [2] y tamaño 100px

label1 = tk.Label(text="A")
label1.grid(row=0,column=0)

label2 = tk.Label(text="B")
label2.grid(row=1,column=0)

window.mainloop()

