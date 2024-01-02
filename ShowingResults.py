import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import StringVar
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import Tk
import sqlite3
from Database import Prop
db = Prop("properties.db")


def connect_db():
    conn = sqlite3.connect('')
    return conn


Results = ctk.CTk()
Results.iconbitmap('favicon.ico')
Results.title("ShowingResults")
Results.geometry('1240x620')
# Results.resizable(False, True)

frame = ctk.CTkScrollableFrame(Results)
frame.pack(pady=20, padx=60, fill="both", expand=True)

tree = Treeview(frame, columns=['id', 'Estate', 'Area',
                'Date', 'Price', 'Status', 'Rooms', 'Location'], show='headings', selectmode='browse')
tree.heading('id', text='ID')
tree.heading('Estate', text='Estate')
tree.heading('Area', text='Area')
tree.heading('Date', text='Date')
tree.heading('Price', text='Price')
tree.heading('Status', text='Status')
tree.heading('Rooms', text='No. Rooms')
tree.heading('Location', text='Location')
tree.column('id', width=30, anchor='center')

tree.pack()

# id = IntVar()
# Estate = StringVar()
# Area = StringVar()
# Date = StringVar()
# Price = StringVar()
# Status = StringVar()
# Rooms = StringVar()
# Location = StringVar()

# def displayAll():
#     tr.delete(*tv.get_children())
#     for row in db.fetch():
#         tv.insert("", END, values=row)

# def get_data(event):
#     global row
#     selected_row =tree.focus()
#     data1 = tree.item(selected_row)
#     row = data1["values"]
#     Estate.set(row[1])
#     Area.set(row[2])
#     Date.set(row[3])
#     Price.set(row[4])
#     Status.set(row[5])
#     Rooms.set(row[6])
#     Location.set(row[7])

estates = [(1, 'Villa', 300, 'Cairo', 7000000, 'Rented', '6', '17-7-2023'),
           (2, 'Room', 100, 'Alexandria', 500, 'availble', '1', '29-12-2023'),
           (3, 'Apartment', 120, 'Giza', 100000, 'availble', '3', '5-9-2023')]

for estate in estates:
    tree.insert('', 'end', iid=estate[0], values=estate)


def displayAll():
    tree.delete(*tree.get_children())
    for row in db.fetch():
        tree.insert("", END, values=row)


displayAll()


def selected():
    if not tree.selection():
        messagebox.showerror("Error", "please select a property")
        return
    print(tree.selection())
    Results.destroy()
    import Payment


btn1 = ctk.CTkButton(Results, text='Select', command=selected)
btn1.pack()


Results.mainloop()
