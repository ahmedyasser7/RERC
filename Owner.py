import customtkinter as ctk
from tkinter import *
from tkinter import StringVar
from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk


OwnerMain = Tk()
OwnerMain.title("Owner")
OwnerMain.geometry('1240x620')
OwnerMain.iconbitmap('favicon.ico')
OwnerMain.resizable(False, True)

# from db import Database
# db =Database("student.db")


def displayAll():
    tv.delete(*tv.get_children())
    # for row in db.fetch():
    #     tv.insert("",END,values=row)


def delete():
    # db.remove(row[0])
    Clear()
    displayAll()


def Clear():
    txtEstate.delete("0", END)
    txtArea.delete("0", END)
    txtLocation.delete("0", END)
    txtPrice.delete("0", END)
    txtStatus.delete("0", END)
    txtRooms.delete("0", END)


def get_data(event):
    selected_row = tv.focus()
    data1 = tv.item(selected_row)
    global row
    row = data1["values"]
    Estate.set(row[1])
    Area.set(row[2])
    Location.set(row[3])
    Price.set(row[4])
    Status.set(row[5])
    Date.set(row[6])


def add():
    if txtEstate.get() == "" or txtArea.get() == "" or txtLocation.get() == "" or txtPrice.get() == "" or txtStatus.get() == "" or txtRooms.get() == "":
        messagebox.showerror("Error", "please fill all the entry")
        return
    # db.insert(

    #     txtEstate.get(),
    #     txtArea.get(),
    #     txtLocation.get(),
    #     txtPrice.get(),
    #     txtStatus.get(),
    #     txtDate.get()
    #     )
    messagebox.showinfo("Success", "Added new proprety")
    Clear()
    displayAll()


def update1():
    if txtEstate.get() == "" or txtArea.get() == "" or txtLocation.get() == "" or txtPrice.get() == "" or txtStatus.get() == "" or txtRooms.get() == "":
        messagebox.showerror("Error", "please fill all the entry")
        return
    # db.update(row[0],
    #     txtEstate.get(),
    #     txtArea.get(),
    #     txtLocation.get(),
    #     txtPrice.get(),
    #     txtStatus.get(),
    #     txtDate.get()
    #     )

    messagebox.showinfo("Success", "the proprety data is updated")
    Clear()
    displayAll()


####### Frame #######
OwnerFrame = Frame(OwnerMain, bg='#252422')
OwnerFrame.place(x=1, y=1, width=1000, height=690)
title = Label(OwnerFrame, text="        Real state rental company         ",
              font=('Calibri', 18, 'bold'), bg='#003566', fg='white')
title.place(x=10, y=1)

id = IntVar()
Estate = StringVar()
Area = StringVar()
Location = StringVar()
Price = StringVar()
Status = StringVar()
Date = StringVar()


lblEstate = Label(OwnerFrame, text="Estate Type:", font=(
    'Calibri bold', 16), bg='#003566', fg='white', bd=1)
lblEstate.place(x=10, y=90)
txtEstate = Entry(OwnerFrame, width=20, font=(
    'Calibri ', 15), textvariable=Estate)
txtEstate.place(x=130, y=90)


lblArea = Label(OwnerFrame, text="Area:            ", font=(
    'Calibri bold', 16), bg='#003566', fg='white', bd=1)
lblArea.place(x=10, y=130)
txtArea = Entry(OwnerFrame, width=20, font=(
    'Calibri ', 15), textvariable=Area)
txtArea.place(x=130, y=130)


lblLocation = Label(OwnerFrame, text="Location:      ", font=(
    'Calibri bold', 16), bg='#003566', fg='white', bd=1)
lblLocation.place(x=10, y=170)
txtLocation = Entry(OwnerFrame, width=20, font=(
    'Calibri ', 15), textvariable=Location)
txtLocation.place(x=130, y=170)

lblPrice = Label(OwnerFrame, text="Price:            ", font=(
    'Calibri bold', 16), bg='#003566', fg='white', bd=1)
lblPrice.place(x=10, y=210)
txtPrice = Entry(OwnerFrame, width=20, font=(
    'Calibri ', 15), textvariable=Price)
txtPrice.place(x=130, y=210)


lblStatus = Label(OwnerFrame, text="Status:          ", font=(
    'Calibri bold', 16), bg='#003566', fg='white', bd=1)
lblStatus.place(x=10, y=250)
txtStatus = ttk.Combobox(OwnerFrame, state='readonly',
                         width=18, font=('Calibri ', 15), textvariable=Status)
txtStatus['values'] = ("available", "Rented")
txtStatus.place(x=130, y=250)


lblRooms = Label(OwnerFrame, text="No. Rooms:  ", font=(
    'Calibri bold', 16), bg='#003566', fg='white', bd=1)
lblRooms.place(x=10, y=290)
txtRooms = Entry(OwnerFrame, width=20, font=(
    'Calibri ', 15), textvariable=Date)
txtRooms.place(x=130, y=290)


lblLocation = Label(OwnerFrame, text="Date:            ", font=(
    'Calibri bold', 16), bg='#003566', fg='white', bd=1)
lblLocation.place(x=10, y=170)
txtLocation = Entry(OwnerFrame, width=20, font=(
    'Calibri ', 15), textvariable=Location)
txtLocation.place(x=130, y=170)
####### Buttons #######
btn_frame = Frame(OwnerFrame, bg='#003566', bd=1, relief=SOLID)
btn_frame.place(x=15, y=390, width=335, height=100)


btnAdd = Button(btn_frame,
                text="Add Details",
                width=14,
                height=1,
                font=("calibri", 16),
                fg='#003566',
                bg='#f6fff8',
                bd=0, command=add
                ).place(x=4, y=5)


btnEdit = Button(btn_frame,
                 text="Update Details",
                 width=14,
                 height=1,
                 font=("calibri", 16),
                 fg='#003566',
                 bg='#f6fff8',
                 bd=0, command=update1
                 ).place(x=4, y=50)


btnDelete = Button(btn_frame,
                   text="Delete Details",
                   width=14,
                   height=1,
                   font=("calibri", 16),
                   fg='#003566',
                   bg='#f6fff8',
                   bd=0, command=delete
                   ).place(x=170, y=5)


btnClear = Button(btn_frame,
                  text="Clear Details",
                  width=14,
                  height=1,
                  font=("calibri", 16),
                  fg='#003566',
                  bg='#f6fff8',
                  bd=0, command=Clear
                  ).place(x=170, y=50)


####### Tree view #######

tree_frame = Frame(OwnerMain, bg='#343a40')
tree_frame.place(x=365, y=1, width=875, height=615)
style = ttk.Style()
# style.theme_use('clam')
style.configure('Treeview', background='#343a40', font=(
    'Arial', 12), rowheight=30, foreground='#e5e5e5')
style.map('Treeview', foreground=[('selected', 'black')], background=[
          ('selected', '#f6fff8')])
style.configure('Treeview.Heading', font=('Arial', 14))
treeScroll = Frame(OwnerMain)
treeScroll.pack(side=RIGHT, fill=Y)
# style.configure("mystyle.Treeview", font=('Calibri', 13), rowheight=50)
# style.configure("mystyle.Treeview.Heading", font=('Calibri', 13))


tv = ttk.Treeview(tree_frame, columns=(
    1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width="30", anchor='c')

tv.heading("2", text="Estate type")
tv.column("2", width="90", anchor='c')

tv.heading("5", text="Price")
tv.column("5", width="90", anchor='c')

tv.heading("3", text="Area")
tv.column("3", width="90", anchor='c')

tv.heading("4", text="location")
tv.column("4", width="90", anchor='c')

tv.heading("6", text="Status")
tv.column("6", width="90", anchor='c')

tv.heading("7", text="No. rooms")
tv.column("7", width="90", anchor='c')

tv.heading("7", text="Date")
tv.column("7", width="90", anchor='c')

tv.heading("8", text="No. Rooms")
tv.column("8", width="90", anchor='c')

tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", get_data)
tv.place(x=1, y=1, height=610, width=875)
displayAll()
OwnerMain.mainloop()
