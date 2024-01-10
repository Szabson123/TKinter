from tkinter import *

root = Tk()
root.config(background='pink')


title = Label(text='Python Mad Libs Game', font=('Helvetica', 24))
title.grid(row=0, column=0)

button1 = Button(text='A memorable Game', background='blue', font=('Helvetica', 16))
button1.grid(row=1, column=0, pady=100)

button2 = Button(text='Ambitions', font=('Helvetica', 16), background='blue')
button2.grid(row=2, column=0, pady=(0, 100))

root.mainloop()

