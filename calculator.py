from tkinter import *

root=Tk()

def count():
    answer = Label(root, text="1", font=("Helvetica", 8))
    answer.grid(row=1, column=0)



titleLabel = Label(root, text="Kalkulator", font=("Helvetica", 14))
titleLabel.grid(row=0, column=0)

button1 = Button(root, text="1", padx=20, pady=20, command=count)
button1.grid(row=2, column=0, sticky="nsew")

button2 = Button(root, text="2", padx=20, pady=20)
button2.grid(row=2, column=1)

button3 = Button(root, text="3", padx=20, pady=20)
button3.grid(row=2, column=2)

button4 = Button(root, text="4", padx=20, pady=20)
button4.grid(row=3, column=0, sticky="nsew")

button5 = Button(root, text="5", padx=20, pady=20)
button5.grid(row=3, column=1)

button6 = Button(root, text="6", padx=20, pady=20)
button6.grid(row=3, column=2)

button7 = Button(root, text="7", padx=20, pady=20)
button7.grid(row=4, column=0, sticky="nsew")

button8 = Button(root, text="8", padx=20, pady=20)
button8.grid(row=4, column=1)

button9 = Button(root, text="9", padx=20, pady=20)
button9.grid(row=4, column=2)


root.mainloop()