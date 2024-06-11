import tkinter as tk
from tkinter import Tk

def selection():
    print("You selected the option:", var.get())
    print(type(var.get()))

root = Tk()
var = tk.IntVar()

radio1 = tk.Radiobutton(root, text="Option 1", variable=var, value="1", command=selection)
radio2 = tk.Radiobutton(root, text="Option 2", variable=var, value="2", command=selection)

radio1.pack()
radio2.pack()

root.mainloop()
