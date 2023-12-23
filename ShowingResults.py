import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import StringVar
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import Tk
import sqlite3


def connect_db():
    conn = sqlite3.connect('')
    return conn


Results = ctk.CTk()
Results.iconbitmap('favicon.ico')
Results.title("ShowingResults")
Results.geometry('800x420')
Results.resizable(False, True)

frame = ctk.CTkScrollableFrame(Results)
frame.pack(pady=20, padx=60, fill="both", expand=True)

tree = Treeview(frame, columns=['id', 'Estate', 'Area',
                'Location', 'Price', 'Status', 'Date'], show='headings', selectmode='browse')
tree.heading('id', text='ID')
tree.heading('Estate', text='Estate')
tree.heading('Area', text='Area')
tree.heading('Location', text='Location')
tree.heading('Price', text='Price')
tree.heading('Status', text='Status')
tree.heading('Date', text='Date')
tree.column('id', width=30, anchor='center')

tree.pack()

estates = [(1, 'Villa', 300, 'Cairo', 7000000, 'Rented', '17-7-2023'),
           (2, 'Room', 100, 'Alexandria', 500, 'availble', '29-12-2023'),
           (3, 'Apartment', 120, 'Giza', 100000, 'availble', '5-9-2023')]

for estate in estates:
    tree.insert('', 'end', iid=estate[0], values=estate)


def selected():
    print(tree.selection())
    Results.destroy()
    import Payment


btn1 = ctk.CTkButton(Results, text='Select', command=selected)
btn1.pack()


Results.mainloop()
