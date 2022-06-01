import time
import random
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import Toplevel, messagebox


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


con = ''
my_cursor = ''


def connect_db():  # for connect button
    def submit_db():
        # fetching the entry values
        global con, my_cursor
        host = host_value.get()
        user = user_value.get()
        password = password_value.get()

        try:
            con = pymysql.connect(host=host, user=user, password=password)
            my_cursor = con.cursor()
        except:
            messagebox.showerror('Notification', 'Data is incorrect Please try again')
            return

        try:
            query = 'create database studentmanagementsystem'
            my_cursor.execute(query=query)
            query1 = 'use studentmanagementsystem'
            my_cursor.execute(query=query1)
            query2 = 'create table studentdata(id int primary key not null, name varchar(20) , mobile varchar(12), ' \
                     'email varchar(30), address varchar(100), gender varchar(10), dob varchar(50), ' \
                     'date varchar(50), time varchar(50))'
            my_cursor.execute(query=query2)

            messagebox.showinfo('Notification', 'Database created and now you are connected to database',
                                parent=db_root)

        except:
            query3 = 'use studentmanagementsystem'
            my_cursor.execute(query3)

            messagebox.showinfo('Notification', 'Database Connected')

        db_root.destroy()

    db_root = Toplevel()
    db_root.config(bg='grey')
    db_root.geometry('500x250+800+100')
    db_root.grab_set()  # nothing will work until you close the top level window
    db_root.iconbitmap('img.ico')
    db_root.resizable(False, False)

    # -------------------------------db labels---------------------
    host_label = Label(db_root, text='Enter Host', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                       width=15, anchor='w')  # anchor is used to move text in particular direction
    host_label.place(x=10, y=10)

    user_label = Label(db_root, text='Enter User', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                       width=15, anchor='w')  # anchor is used to move text in particular direction
    user_label.place(x=10, y=60)

    password_label = Label(db_root, text='Enter Password', bg='cyan', font='times 15 bold', relief=GROOVE,
                           borderwidth=3, width=15, anchor='w')  # anchor is used to move text in particular direction
    password_label.place(x=10, y=110)

    # -------------------------------db labels---------------------
    host_value = StringVar()
    user_value = StringVar()
    password_value = StringVar()

    host_entry = Entry(db_root, textvariable=host_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    host_entry.place(x=250, y=10)

    user_entry = Entry(db_root, textvariable=user_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    user_entry.place(x=250, y=60)

    password_entry = Entry(db_root, textvariable=password_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    password_entry.place(x=250, y=110)

    # -------------------------------connect button---------------------
    submit_button = Button(db_root, text='Connect', font='roman 15 bold', width=15, bd=5, activebackground='red',
                           activeforeground='white', bg='powderblue', command=submit_db)
    submit_button.place(x=150, y=180)

    db_root.mainloop()


# -----------------------------------function for data entry labels---------------------------------
def add_student():
    def submit_add():
        id = id_value.get()
        name = name_value.get()
        mobile = mobile_value.get()
        email = email_value.get()
        address = address_value.get()
        gender = gender_value.get()
        dob = dob_value.get()
        added_time = time.strftime("%H:%M:%S")
        added_date = time.strftime("%d/%m/%Y")
        try:
            query = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            my_cursor.execute(query, (id, name, mobile, email, address, gender, dob, added_date, added_time))
            con.commit()
            res = messagebox.askyesnocancel('Notification', 'Id {} Name {} Added successfully.. and want to / '
                                                            'clean form'.format(id, name), parent=add_root)
            if res:
                id_value.set('')
                name_value.set('')
                mobile_value.set('')
                email_value.set('')
                address_value.set('')
                gender_value.set('')
                dob_value.set('')
        except:
            messagebox.showerror('Notification', 'Id already exist try other Id...', parent=add_root)

        query1 = 'select * from studentdata'
        my_cursor.execute(query1)
        data = my_cursor.fetchall()
        student_table.delete(*student_table.get_children())
        for i in data:
            lst = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            student_table.insert('', END, values=lst)

    add_root = Toplevel(master=DataEntryFrame)
    add_root.config(bg='grey')
    add_root.geometry('500x450+100+100')
    add_root.grab_set()  # nothing will work until you close the top level window
    add_root.iconbitmap('img.ico')
    add_root.resizable(False, False)

    # -----------------------------------add student labels---------------------------------
    id_label = Label(add_root, text='Enter Id', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                     width=15, anchor='w')  # anchor is used to move text in particular direction
    id_label.place(x=10, y=10)

    name_label = Label(add_root, text='Enter Name', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                       width=15, anchor='w')
    name_label.place(x=10, y=60)

    mobile_label = Label(add_root, text='Enter Mobile', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                         width=15, anchor='w')
    mobile_label.place(x=10, y=110)

    email_label = Label(add_root, text='Enter Email', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                        width=15, anchor='w')
    email_label.place(x=10, y=160)

    address_label = Label(add_root, text='Enter Address', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                          width=15, anchor='w')
    address_label.place(x=10, y=210)

    gender_label = Label(add_root, text='Enter Gender', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                         width=15, anchor='w')
    gender_label.place(x=10, y=260)

    dob_label = Label(add_root, text='Enter D.O.B', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                      width=15, anchor='w')
    dob_label.place(x=10, y=310)

    # -----------------------------------add student entry---------------------------------
    id_value = StringVar()
    name_value = StringVar()
    mobile_value = StringVar()
    email_value = StringVar()
    address_value = StringVar()
    gender_value = StringVar()
    dob_value = StringVar()

    id_entry = Entry(add_root, textvariable=id_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    id_entry.place(x=250, y=10)

    name_entry = Entry(add_root, textvariable=name_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    name_entry.place(x=250, y=60)

    mobile_entry = Entry(add_root, textvariable=mobile_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    mobile_entry.place(x=250, y=110)

    email_entry = Entry(add_root, textvariable=email_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    email_entry.place(x=250, y=160)

    address_entry = Entry(add_root, textvariable=address_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    address_entry.place(x=250, y=210)

    gender_entry = Entry(add_root, textvariable=gender_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    gender_entry.place(x=250, y=260)

    dob_entry = Entry(add_root, textvariable=dob_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    dob_entry.place(x=250, y=310)

    # -------------------------------submit button--------------------------
    submit_button = Button(add_root, text='Submit', font='roman 15 bold', width=20, bd=5, activebackground='red',
                           activeforeground='white', bg='powderblue', command=submit_add)
    submit_button.place(x=150, y=380)

    add_root.mainloop()


def search_student():
    def submit_search():
        id_value.get()
        name_value.get()
        mobile_value.get()
        email_value.get()
        address_value.get()
        gender_value.get()
        dob_value.get()
        date_value.get()

    search_root = Toplevel(master=DataEntryFrame)
    search_root.config(bg='grey')
    search_root.geometry('500x500+100+100')
    search_root.grab_set()  # nothing will work until you close the top level window
    search_root.iconbitmap('img.ico')
    search_root.resizable(False, False)

    # -----------------------------------search student labels---------------------------------
    id_label = Label(search_root, text='Enter Id', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                     width=15, anchor='w')  # anchor is used to move text in particular direction
    id_label.place(x=10, y=10)

    name_label = Label(search_root, text='Enter Name', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                       width=15, anchor='w')
    name_label.place(x=10, y=60)

    mobile_label = Label(search_root, text='Enter Mobile', bg='cyan', font='times 15 bold', relief=GROOVE,
                         borderwidth=3,
                         width=15, anchor='w')
    mobile_label.place(x=10, y=110)

    email_label = Label(search_root, text='Enter Email', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                        width=15, anchor='w')
    email_label.place(x=10, y=160)

    address_label = Label(search_root, text='Enter Address', bg='cyan', font='times 15 bold', relief=GROOVE,
                          borderwidth=3,
                          width=15, anchor='w')
    address_label.place(x=10, y=210)

    gender_label = Label(search_root, text='Enter Gender', bg='cyan', font='times 15 bold', relief=GROOVE,
                         borderwidth=3,
                         width=15, anchor='w')
    gender_label.place(x=10, y=260)

    dob_label = Label(search_root, text='Enter D.O.B', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                      width=15, anchor='w')
    dob_label.place(x=10, y=310)

    date_label = Label(search_root, text='Enter Date', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                       width=15, anchor='w')
    date_label.place(x=10, y=360)

    # -----------------------------------search student entry---------------------------------
    id_value = StringVar()
    name_value = StringVar()
    mobile_value = StringVar()
    email_value = StringVar()
    address_value = StringVar()
    gender_value = StringVar()
    dob_value = StringVar()
    date_value = StringVar()

    id_entry = Entry(search_root, textvariable=id_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    id_entry.place(x=250, y=10)

    name_entry = Entry(search_root, textvariable=name_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    name_entry.place(x=250, y=60)

    mobile_entry = Entry(search_root, textvariable=mobile_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    mobile_entry.place(x=250, y=110)

    email_entry = Entry(search_root, textvariable=email_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    email_entry.place(x=250, y=160)

    address_entry = Entry(search_root, textvariable=address_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    address_entry.place(x=250, y=210)

    gender_entry = Entry(search_root, textvariable=gender_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    gender_entry.place(x=250, y=260)

    dob_entry = Entry(search_root, textvariable=dob_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    dob_entry.place(x=250, y=310)

    date_entry = Entry(search_root, textvariable=date_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    date_entry.place(x=250, y=360)

    # -------------------------------submit button--------------------------
    submit_button = Button(search_root, text='Submit', font='roman 15 bold', width=20, bd=5, activebackground='red',
                           activeforeground='white', bg='powderblue', command=submit_search)
    submit_button.place(x=150, y=430)

    search_root.mainloop()


def delete_student():
    pass


def update_student():
    def submit_update():
        pass

    update_root = Toplevel(master=DataEntryFrame)
    update_root.config(bg='grey')
    update_root.geometry('500x550+100+100')
    update_root.grab_set()  # nothing will work until you close the top level window
    update_root.iconbitmap('img.ico')
    update_root.resizable(False, False)

    # -----------------------------------update student labels---------------------------------
    id_label = Label(update_root, text='Update Id', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                     width=15, anchor='w')  # anchor is used to move text in particular direction
    id_label.place(x=10, y=10)

    name_label = Label(update_root, text='Enter Name', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                       width=15, anchor='w')
    name_label.place(x=10, y=60)

    mobile_label = Label(update_root, text='Update Mobile', bg='cyan', font='times 15 bold', relief=GROOVE,
                         borderwidth=3,
                         width=15, anchor='w')
    mobile_label.place(x=10, y=110)

    email_label = Label(update_root, text='Update Email', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                        width=15, anchor='w')
    email_label.place(x=10, y=160)

    address_label = Label(update_root, text='Update Address', bg='cyan', font='times 15 bold', relief=GROOVE,
                          borderwidth=3,
                          width=15, anchor='w')
    address_label.place(x=10, y=210)

    gender_label = Label(update_root, text='Update Gender', bg='cyan', font='times 15 bold', relief=GROOVE,
                         borderwidth=3,
                         width=15, anchor='w')
    gender_label.place(x=10, y=260)

    dob_label = Label(update_root, text='Update D.O.B', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                      width=15, anchor='w')
    dob_label.place(x=10, y=310)

    date_label = Label(update_root, text='Update Date', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                       width=15, anchor='w')
    date_label.place(x=10, y=360)

    time_label = Label(update_root, text='Update Time', bg='cyan', font='times 15 bold', relief=GROOVE, borderwidth=3,
                       width=15, anchor='w')
    time_label.place(x=10, y=410)

    # -----------------------------------update student entry---------------------------------
    id_value = StringVar()
    name_value = StringVar()
    mobile_value = StringVar()
    email_value = StringVar()
    address_value = StringVar()
    gender_value = StringVar()
    dob_value = StringVar()
    date_value = StringVar()
    time_value = StringVar()

    id_entry = Entry(update_root, textvariable=id_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    id_entry.place(x=250, y=10)

    name_entry = Entry(update_root, textvariable=name_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    name_entry.place(x=250, y=60)

    mobile_entry = Entry(update_root, textvariable=mobile_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    mobile_entry.place(x=250, y=110)

    email_entry = Entry(update_root, textvariable=email_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    email_entry.place(x=250, y=160)

    address_entry = Entry(update_root, textvariable=address_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    address_entry.place(x=250, y=210)

    gender_entry = Entry(update_root, textvariable=gender_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    gender_entry.place(x=250, y=260)

    dob_entry = Entry(update_root, textvariable=dob_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    dob_entry.place(x=250, y=310)

    date_entry = Entry(update_root, textvariable=date_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    date_entry.place(x=250, y=360)

    time_entry = Entry(update_root, textvariable=time_value, font='roman 15 bold', relief=SUNKEN, bd=3)
    time_entry.place(x=250, y=410)

    # -------------------------------submit button--------------------------
    submit_button = Button(update_root, text='Submit', font='roman 15 bold', width=20, bd=5, activebackground='red',
                           activeforeground='white', bg='powderblue', command=submit_update)
    submit_button.place(x=150, y=480)

    update_root.mainloop()


def show_student():
    pass


def export_student():
    pass


def exit_student():
    result = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if result:
        root.destroy()


root = Tk()
root.title('Student Management System')
root.config(bg='grey')
root.geometry('1500x770+10+10')
root.iconbitmap('img.ico')
root.resizable(False, False)

# -----------------------------------Data Entry Frames and labels-----------------------------------
DataEntryFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=100, width=500, height=650)

add_button = Button(DataEntryFrame, text='1. Add Student', width=25, font='chiller 20 bold', bd=6, bg='skyblue3',
                    activebackground='blue', activeforeground='white', relief=RAISED, command=add_student)
add_button.pack(side=TOP, expand=True)

search_button = Button(DataEntryFrame, text='2. Search Student', width=25, font='chiller 20 bold', bd=6, bg='skyblue3',
                       activebackground='blue', activeforeground='white', relief=RAISED, command=search_student)
search_button.pack(side=TOP, expand=True)

delete_button = Button(DataEntryFrame, text='3. Delete Student', width=25, font='chiller 20 bold', bd=6, bg='skyblue3',
                       activebackground='blue', activeforeground='white', relief=RAISED, command=delete_student)
delete_button.pack(side=TOP, expand=True)

update_button = Button(DataEntryFrame, text='4. Update Student', width=25, font='chiller 20 bold', bd=6, bg='skyblue3',
                       activebackground='blue', activeforeground='white', relief=RAISED, command=update_student)
update_button.pack(side=TOP, expand=True)

show_button = Button(DataEntryFrame, text='5. Show All', width=25, font='chiller 20 bold', bd=6, bg='skyblue3',
                     activebackground='blue', activeforeground='white', relief=RAISED, command=show_student)
show_button.pack(side=TOP, expand=True)

export_button = Button(DataEntryFrame, text='6. Export Data', width=25, font='chiller 20 bold', bd=6, bg='skyblue3',
                       activebackground='blue', activeforeground='white', relief=RAISED, command=export_student)
export_button.pack(side=TOP, expand=True)

exit_button = Button(DataEntryFrame, text='7. Exit', width=25, font='chiller 20 bold', bd=6, bg='skyblue3',
                     activebackground='blue', activeforeground='white', relief=RAISED, command=exit_student)
exit_button.pack(side=TOP, expand=True)

# -----------------------------------Show Data Frame-----------------------------------
ShowDataFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=600, y=100, width=890, height=650)

# -----------------------------------Creating Tree view in show dataframe-----------------------------------
style = ttk.Style()
style.configure('Treeview.Heading', font='chiller 20 bold', foreground='blue')  # change style of tree view headings
style.configure('Treeview', font='times 15 bold', foreground='black', background='cyan')  # style of data in tree view

scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
student_table = Treeview(ShowDataFrame, columns=('Id', 'Name', 'Mobile No.', 'Email', 'Address', 'Gender', 'D.O.B',
                                                 'Added Date', 'Added Time'), yscrollcommand=scroll_y.set,
                         xscrollcommand=scroll_x.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)

# ----------------set the headings--------------------
student_table.heading('Id', text='Id')
student_table.heading('Name', text='Name')
student_table.heading('Mobile No.', text='Mobile No.')
student_table.heading('Email', text='Email')
student_table.heading('Address', text='Address')
student_table.heading('Gender', text='Gender')
student_table.heading('D.O.B', text='D.O.B')
student_table.heading('Added Date', text='Added Date')
student_table.heading('Added Time', text='Added Time')

student_table['show'] = 'headings'  # show only headings remove extra column

# ---------set width of columns-------------
student_table.column('Id', width=50)
student_table.column('Name', width=200)
student_table.column('Mobile No.', width=120)
student_table.column('Email', width=250)
student_table.column('Address', width=250)
student_table.column('Gender', width=100)
student_table.column('D.O.B', width=150)
student_table.column('Added Date', width=170)
student_table.column('Added Time', width=150)

student_table.pack(fill=BOTH, expand=1)

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
