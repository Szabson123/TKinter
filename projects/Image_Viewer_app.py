from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Icons an Images")
root.iconbitmap('C:/Users/szaba/Documents/icona.ico')

my_img1 = ImageTk.PhotoImage(Image.open('basics/images/icona1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('basics/images/icona2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('basics/images/icona3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('basics/images/icona4.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('basics/images/icona5.jpg'))


my_label = Label(image=my_img1)
my_label.pack()


button_quit = Button(root, text='Exit Program', font=('Helvetica', 12), command=root.quit)
button_quit.pack()

root.mainloop()