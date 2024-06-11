import tkinter as tk
from tkinter import Tk

def get_selection():
    selection = listbox.curselection()
    if selection:
        print("Selected item:", listbox.get(selection[0]))

root = Tk()
listbox = tk.Listbox(root)
options = ["Option 1", "Option 2", "Option 3"]

for option in options:
    listbox.insert(tk.END, option)

listbox.pack()
button = tk.Button(root, text="Get Selection", command=get_selection)
button.pack()

root.mainloop()
