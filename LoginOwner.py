import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import sqlite3

OwnerLogin = ctk.CTk()
OwnerLogin.title("LoginOwner")
OwnerLogin.geometry("600x450")
OwnerLogin.iconbitmap('favicon.ico')
OwnerLogin.resizable(False, True)


frame = ctk.CTkScrollableFrame(OwnerLogin)
frame.pack(pady=20, padx=60, fill="both", expand=True)

TheLabel = ctk.CTkLabel(frame, text="Hello our Partner!")
TheLabel.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(frame, placeholder_text="ID")
entry2 = ctk.CTkEntry(frame, placeholder_text="Password", show="*")

entry1.pack(pady=12, padx=10)
entry2.pack(pady=12, padx=10)


def connect_db():
    conn = sqlite3.connect('OwnerData.py')
    return conn


# con = connect_db()
# cursor = con.cursor()
# cursor.execute(
#     "CREATE TABLE if not exists OwnerData (ID INTEGER, password TEXT)"
# )
# cursor.execute("INSERT INTO OwnerData VALUES (?, ?)",
#                (1, 123))
# cursor.execute("INSERT INTO OwnerData VALUES (?, ?)",
#                (2, 456))
# cursor.execute("INSERT INTO OwnerData VALUES (?, ?)",
#                (3, 789))
# cursor.execute("INSERT INTO OwnerData VALUES (?, ?)",
#                (4, 2468))
# con.commit()
# con.close()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


def login():
    ID = entry1.get()
    password = entry2.get()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE if not exists OwnerData (ID INTEGER, password INTEGER)"
    )
    cursor.execute(
        "SELECT * FROM OwnerData WHERE ID = ? AND password = ?", (ID, password))
    result = cursor.fetchone()
    if result is None:
        messagebox.showerror("Error", "Invalid ID or password.")
    else:
        messagebox.showinfo("Success", "Logged in successfully!")
        OwnerLogin.destroy()
        import Owner
    conn.commit()
    conn.close()


button1 = ctk.CTkButton(frame, text="Login", command=login)
button1.pack(pady=12, padx=10)

checkBox = ctk.CTkCheckBox(frame, text="Stay Signed?")
checkBox.pack(pady=12, padx=10)

OwnerLogin.mainloop()
