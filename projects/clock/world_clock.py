from tkinter import *
from datetime import datetime
import time
import pytz


def world_main():
    worldRoot = Toplevel()
    worldRoot.title('World Clock')
    worldRoot.config(background='black')
    worldRoot.geometry('600x400')
    timezone_london = 'Europe/London'
    timezone_warsaw = 'Europe/Warsaw'
    timezone_seoul = 'Asia/Seoul'
    
    def get_time(timezone):
        london = datetime.now(pytz.timezone(timezone))
        warsaw = datetime.now(pytz.timezone(timezone))
        seoul = datetime.now(pytz.timezone(timezone))
        return london.strftime("%H:%M:%S"), seoul.strftime("%H:%M:%S"), warsaw.strftime("%H:%M:%S")


    
    def update_labels():
        london_label.config(text=get_time(timezone))
        london_label.after(1000, update_labels)
        
    
    london_label = Label(worldRoot, font=('calibri', 40, 'bold'), background='purple', foreground='white')
    london_label.grid(row=0, column=0)
    update_labels()
        

    

