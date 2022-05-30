from tkinter import *
import time
import random
from tkinter import Toplevel


def date_time():  # for configure clock
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d-%m-%Y")
    clock.config(text='Date : ' + date_string + '\n' + 'Time : ' + time_string)
    clock.after(200, date_time)


def intro_label():  # for configure slider
    global count, text
    if count >= len(ss):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text + ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(100, intro_label)


colors = ['red', 'green', 'blue']


def intro_label_color():  # for colorize slider
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(20, intro_label_color)


def connect_db():  # for connect button
    db_root = Toplevel()
    db_root.config(bg='black')
    db_root.geometry('500x300+800+100')
    db_root.grab_set()  # nothing will work until you close the top level window
    db_root.iconbitmap('img.ico')
    db_root.resizable(False, False)

    # -------------------------------db labels---------------------
    host_label = Label(db_root, text='Enter Host', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                       width=15, anchor='w')  # anchor is used to move text in particular direction
    host_label.place(x=10, y=10)

    user_label = Label(db_root, text='Enter User', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                       width=15, anchor='w')  # anchor is used to move text in particular direction
    user_label.place(x=10, y=80)

    password_label = Label(db_root, text='Enter Password', bg='cyan', font='times 15 bold', relief=GROOVE,
                           borderwidth=3, width=15, anchor='w')  # anchor is used to move text in particular direction
    password_label.place(x=10, y=150)

    # -------------------------------db labels---------------------
    host_value = StringVar()
    user_value = StringVar()
    password_value = StringVar()

    host_entry = Entry(db_root, textvariable=host_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    host_entry.place(x=250, y=10)

    user_entry = Entry(db_root, textvariable=user_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    user_entry.place(x=250, y=80)

    password_entry = Entry(db_root, textvariable=password_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    password_entry.place(x=250, y=150)

    # -------------------------------connect button---------------------
    submit_button = Button(db_root, text='Connect', font='roman 20 bold', width=15, activebackground='red',
                           activeforeground='white')
    submit_button.place(x=150, y=210)
    db_root.mainloop()


root = Tk()
root.title('Student Management System')
root.config(bg='black')
root.geometry('1500x770+10+10')
root.iconbitmap('img.ico')
root.resizable(False, False)

# -----------------------------------Data Entry Frames and labels-----------------------------------
DataEntryFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=100, width=600, height=650)

add_button = Button(DataEntryFrame, text='1. Add Student', width=25, font='chiller 20 bold', bd=6, bg='skyblue3',
                    activebackground='blue', activeforeground='white', relief=RIDGE)
add_button.pack(side=TOP, expand=True)

search_button = Button(DataEntryFrame, text='2. Search Student', width=25, font='chiller 20 bold', bd=6, bg='skyblue3',
                       activebackground='blue', activeforeground='white', relief=RIDGE)
search_button.pack(side=TOP, expand=True)

delete_button = Button(DataEntryFrame, text='3. Delete Student', width=25, font='chiller 20 bold', bd=6, bg='skyblue3',
                       activebackground='blue', activeforeground='white', relief=RIDGE)
delete_button.pack(side=TOP, expand=True)

update_button = Button(DataEntryFrame, text='4. Update Student', width=25, font='chiller 20 bold', bd=6, bg='skyblue3',
                       activebackground='blue', activeforeground='white', relief=RIDGE)
update_button.pack(side=TOP, expand=True)

show_button = Button(DataEntryFrame, text='5. Show All', width=25, font='chiller 20 bold', bd=6, bg='skyblue3',
                     activebackground='blue', activeforeground='white', relief=RIDGE)
show_button.pack(side=TOP, expand=True)

export_button = Button(DataEntryFrame, text='6. Export Data', width=25, font='chiller 20 bold', bd=6, bg='skyblue3',
                       activebackground='blue', activeforeground='white', relief=RIDGE)
export_button.pack(side=TOP, expand=True)

exit_button = Button(DataEntryFrame, text='7. Exit', width=25, font='chiller 20 bold', bd=6, bg='skyblue3',
                     activebackground='blue', activeforeground='white', relief=RIDGE)
exit_button.pack(side=TOP, expand=True)

# -----------------------------------Show Data Frame-----------------------------------
ShowDataFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=700, y=100, width=790, height=650)

# -----------------------------------Slider-----------------------------------
ss = 'Welcome To Student Management System'
count = 0
text = ''

SliderLabel = Label(root, text=ss, relief=RIDGE, font='chiller 30 italic bold', borderwidth=4, width=35, bg='cyan')
SliderLabel.place(x=450, y=0)

intro_label()  # function calling
intro_label_color()

# -----------------------------------Clock-----------------------------------
clock = Label(root, text='', font='times 15 bold', relief=SUNKEN, borderwidth=6, bg='cyan', width=15, )
clock.place(x=0, y=0)

date_time()  # function calling

# -----------------------------------Connect database button-----------------------------------
Connect_Button = Button(root, text='Connect To Database', font='times 15 bold', relief=SUNKEN, borderwidth=6, bg='cyan',
                        width=15, activebackground='grey', activeforeground='white', command=connect_db)
Connect_Button.place(x=1300, y=0)

root.mainloop()
