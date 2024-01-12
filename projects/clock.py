from tkinter import *
import time

root = Tk()
root.title('Clock')
root.geometry('600x400')
root.config(background='black')

def clock():
  pass




clock_label = Label(root, text='', font=('Helvetica', 24), background='grey', fg='yellow')
clock_label.grid(row=0, column=0)



root.mainloop()