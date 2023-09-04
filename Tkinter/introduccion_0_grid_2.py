import tkinter as tk
window = tk.Tk()
window.columnconfigure(0,minsize=250)
window.rowconfigure([0,1,2],minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0,column=0,sticky="n")

label2 = tk.Label(text="B")
label2.grid(row=1,column=0,sticky="w")

label3 = tk.Label(text="C")
label3.grid(row=2,column=0,sticky="se")
window.mainloop()