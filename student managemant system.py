import tkinter
from tkinter import *
import time
root = Tk()
root.title('Student Management System')
root.config(bg='black')
root.geometry('1500x770+10+10')
root.iconbitmap('img.ico')
root.resizable(False, False)

# -----------------------------------Frames-----------------------------------
DataEntryFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=100, width=600, height=650)

ShowDataFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=700, y=100, width=790, height=650)

# -----------------------------------Slider-----------------------------------
ss = 'Welcome To Student Management System'

SliderLabel = Label(root, text=ss, relief=RIDGE, font='chiller 30 italic bold', borderwidth=5, width=35)
SliderLabel.place(x=260)
root.mainloop()
