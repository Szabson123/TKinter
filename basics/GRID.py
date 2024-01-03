from tkinter import *

root = Tk()

firstLabel = Label(root, text="Siemano")
scLabel = Label(root, text="Hejo Hejo")

firstLabel.grid(row=0, column=0)
scLabel.grid(row=1, column=1)

root.mainloop()