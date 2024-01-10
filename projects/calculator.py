from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)


def count(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    sth = e.insert(0, str(current) + str(number))
    return sth


def clear():
    e.delete(0, END)


def equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, f_num + int(second_number))

    if math == "divide":
        if int(second_number) == 0:
            e.insert(0, "You cant divide by 0")
        else:
            e.insert(0, f_num / int(second_number))

    if math == "subtract":
        e.insert(0, f_num - int(second_number))

    if math == "multiply":
        e.insert(0, f_num * int(second_number))


def add():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)


def divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)


def subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    e.delete(0, END)


def multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)


button1 = Button(root, text="1", padx=40, pady=20, command=lambda: count(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: count(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: count(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: count(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: count(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: count(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: count(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: count(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: count(9))
buttonclear = Button(root, text="C", padx=87, pady=20, command=clear)
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: count(0))
buttoneven = Button(root, text="=", padx=87, pady=20, command=equal)
buttonadd = Button(root, text="+", padx=40, pady=20, command=add)
button_divide = Button(root, text="/", padx=40, pady=20, command=divide)
button_subtract = Button(root, text="-", padx=40, pady=20, command=subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=multiply)

button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button7.grid(row=4, column=0)
button8.grid(row=4, column=1)
button9.grid(row=4, column=2)
buttonclear.grid(row=5, column=1, columnspan=2)
button0.grid(row=5, column=0)
buttoneven.grid(row=6, column=1, columnspan=2)
buttonadd.grid(row=6, column=0)
button_divide.grid(row=7, column=0)
button_subtract.grid(row=7, column=1)
button_multiply.grid(row=7, column=2)


root.mainloop()
