from tkinter import Tk, Frame, Label, Button, Entry, Text, Radiobutton,Checkbutton, Listbox, Canvas, Scale, Spinbox, OptionMenu, IntVar, StringVar
from tkinter.ttk import Combobox
window = Tk()
# Frame
frame = Frame(window)
frame.pack()
# Label
label = Label(frame, text="Hello, World!")
label.pack()
# Button
button = Button(frame, text="Click Me")
button.pack()
# Entry
entry = Entry(frame)
entry.pack()
# Text
text = Text(frame)
text.pack()
# Radiobutton
var = IntVar()
rb1 = Radiobutton(frame, text="Option 1", variable=var, value=1)
rb2 = Radiobutton(frame, text="Option 2", variable=var, value=2)
rb1.pack()
rb2.pack()
# Checkbutton
var_check = IntVar()
checkbutton = Checkbutton(frame, text="Check me", variable=var_check)
checkbutton.pack()

# OptionMenu
var_option = StringVar(frame)
var_option.set("Option 1")
optionmenu = OptionMenu(frame, var_option, "Option 1", "Option 2", "Option3")
optionmenu.pack()
# Scale
scale = Scale(frame, from_=0, to=100)
scale.pack()
# Canvas
canvas = Canvas(frame, width=200, height=200)
canvas.create_line(0, 0, 200, 200)
canvas.pack()

# Combobox
combobox = Combobox(frame)
combobox['values'] = ("Option 1", "Option 2", "Option 3")
combobox.pack()
# Spinbox
spinbox = Spinbox(frame, from_=0, to=10)
spinbox.pack()

window.mainloop()


