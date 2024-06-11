from tkinter import Tk, StringVar, Entry, Label

def main():
    # Create the main window
    root = Tk()
    root.title("Simple StringVar Example")

    # Create a StringVar instance
    var = StringVar()

    # Create and pack an Entry widget using the StringVar
    entry = Entry(root, textvariable=var)
    entry.pack()

    # Create and pack a Label widget that updates with the StringVar
    label = Label(root, textvariable=var)
    label.pack()
    label2 = Label(root, text="bruh")
    label2.pack()
    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()
