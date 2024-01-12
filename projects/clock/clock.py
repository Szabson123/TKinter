from tkinter import *
import time
from world_clock import world_main

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


clock_label = Label(root, text='', font=('Helvetica', 32), background='black', fg='yellow')
clock_label.grid(row=0, column=0, sticky="nsew", pady=40)
root.grid_columnconfigure(0, weight=1)


world_clock = Button(root, text='World Clocks', font=('Helvetica', 24), background='black', fg='yellowgreen', command=world_main)
world_clock.grid(row=1, column=0, pady=10)

timer = Button(root, text='Timer', font=('Helvetica', 24), background='black', fg='yellowgreen')
timer.grid(row=2, column=0, pady=10)

alarm_clock = Button(root, text='Alarm Clock', font=('Helvetica', 24), background='black', fg='yellowgreen')
alarm_clock.grid(row=3, column=0, pady=10)



clock()


root.mainloop()