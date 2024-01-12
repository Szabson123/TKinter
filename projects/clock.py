from tkinter import *
import time

root = Tk()
root.title('Clock')
root.geometry('600x400')
root.config(background='black')

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    
    clock_label.config(text=f'{hour}:{minute}:{second}')
    
    clock_label.after(1000, clock)


clock_label = Label(root, text='', font=('Helvetica', 24), background='black', fg='yellow')
clock_label.grid(row=0, column=0, sticky="nsew", pady=40)
root.grid_columnconfigure(0, weight=1)



clock()


root.mainloop()