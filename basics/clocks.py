from tkinter import *
import time



root = Tk()
root.title('clocks')
root.geometry('1600x400')

def update():
    my_label.config(text='New Text')


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    secound = time.strftime("%S")
    day = time.strftime("%A")
    time_zone = time.strftime("%Z")
    week_number = time.strftime("%U")
    
    my_label.config(text=f"{hour}:{minute}:{secound} - {time_zone}\n{day}")
    my_label.after(1000, clock)
    
    my_label_two.config(text=f'{week_number}')
    my_label_two.after(1000, clock)

my_label = Label(root, text='', font=('Helvetica', 48), fg='green', bg='black')
my_label.pack(pady=20)

my_label_two = Label(root, text='', font=('Helvetica', 18))
my_label_two.pack(pady=10)

clock()
#my_label.after(5000, update)


root.mainloop()