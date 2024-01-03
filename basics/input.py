from tkinter import *

root = Tk()
e = Entry(root, width=50, borderwidth=5)
e.grid(row=1, column=1)
e.insert(0, "Write here: ")

def clicked():
    hello = f"Hello {e.get()}"
    myLabel = Label(root, text=hello)
    myLabel.grid(row=2, column=1)

myButton = Button(root, text="Click me!", state=DISABLED, padx=50, pady=50)
myButton2 = Button(root, text="Enter your name", command=clicked, fg="blue", bg="yellow")
myButton.grid(row=0 ,column=0)
myButton2.grid(row=3 ,column=0)

root.mainloop()