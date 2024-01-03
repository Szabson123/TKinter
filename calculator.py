from tkinter import *

root=Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)

def count():
    answer = Label(root, text="1", font=("Helvetica", 8))
    answer.grid(row=1, column=0)

button1 = Button(root, text="1", padx=40, pady=20)
button2 = Button(root, text="2", padx=40, pady=20)
button3 = Button(root, text="3", padx=40, pady=20)
button4 = Button(root, text="4", padx=40, pady=20)
button5 = Button(root, text="5", padx=40, pady=20)
button6 = Button(root, text="6", padx=40, pady=20)
button7 = Button(root, text="7", padx=40, pady=20)
button8 = Button(root, text="8", padx=40, pady=20)
button9 = Button(root, text="9", padx=40, pady=20)
buttonclear = Button(root, text="C", padx=80, pady=20)
button0 = Button(root, text="0", padx=40, pady=20)
buttonadd = Button(root, text="+", padx=40, pady=20)
buttoneven = Button(root, text="=", padx=80, pady=20)

button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button7.grid(row=4, column=0)
button8.grid(row=4, column=1)
button9.grid(row=4, column=2)
buttonclear.grid(row=5, column=1)
button0.grid(row=5, column=0)
buttoneven.grid(row=6, column=1)
buttonadd.grid(row=6, column=0)


root.mainloop()