from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Icons an Images")
root.iconbitmap('C:/Users/szaba/Documents/icona.ico')

my_img = ImageTk.PhotoImage(Image.open('basics/images/icona.jpg'))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text='Exit Program', font=('Helvetica', 12), command=root.quit)
button_quit.pack()

root.mainloop()