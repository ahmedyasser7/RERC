import customtkinter as ctk
import tkinter as tk
import sqlite3


def connect_db():
    conn = sqlite3.connect('')
    return conn


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

Choose = ctk.CTk()
Choose.title("Choose")
Choose.geometry("350x200")
Choose.iconbitmap('favicon.ico')
Choose.resizable(False, True)

frame = ctk.CTkFrame(Choose)
frame.pack(fill="both", expand=True)


def Rentment():
    # Modify here!
    pass


def Cancel():
    Choose.destroy()
    import SuccessfulOperation


button1 = ctk.CTkButton(frame, text="Rentment", command=Rentment)
button1.pack(pady=30, padx=10)


button2 = ctk.CTkButton(frame, text="Cancel", command=Cancel)
button2.pack(pady=10, padx=10)

Choose.mainloop()
