import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import StringVar
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import Tk

Results = ctk.CTk()
Results.iconbitmap('favicon.ico')
Results.title("ShowingResults")
Results.geometry('800x420')
Results.resizable(False, True)

frame = ctk.CTkScrollableFrame(Results)
frame.pack(pady=20, padx=60, fill="both", expand=True)
estates = [(1, 'Villa', 230, 'Cairo', 1200, 'Rented', '17-7-2023'),
           ]
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

for estate in estates:
    tree.insert('', 'end', iid=estate[0], values=estates)


def selected():
    print(tree.selection())
    Results.destroy()
    import Payment


btn1 = ctk.CTkButton(Results, text='Select', command=selected)
btn1.pack()


Results.mainloop()
