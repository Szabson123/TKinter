from tkinter import *

root = Tk()

def clicked():
    myLabel = Label(root, text="Hello someone clicked me")
    myLabel.grid(row=2, column=1)

myButton = Button(root, text="Click me!", state=DISABLED, padx=50, pady=50)
myButton2 = Button(root, text="Click me!", command=clicked, fg="blue", bg="yellow")
myButton.grid(row=0 ,column=0)
myButton2.grid(row=1 ,column=0)

root.mainloop()