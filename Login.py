import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

UserLogin = ctk.CTk()
UserLogin.title("Login")
UserLogin.geometry("600x450")
UserLogin.iconbitmap('favicon.ico')
UserLogin.resizable(False, True)


def connect_db():
    conn = sqlite3.connect('users.db')
    return conn


con = connect_db()


def login():
    username = username_entry.get()
    password = password_entry.get()
    conn = connect_db()
    cursor = conn.cursor()
    # cursor.execute(
    #     "CREATE TABLE if not exists UserData (username TEXT, password INTEGER)"
    # )
    cursor.execute(
        "SELECT * FROM UserData WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()

    if result is None:
        messagebox.showerror("Error", "Invalid username or password.")
    else:
        messagebox.showinfo("Success", "Logged in successfully!")
        UserLogin.destroy()
        import Search

    conn.close()


def create_account():
    pass
    username = username_entry.get()
    password = password_entry.get()

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO UserData VALUES (?, ?)",
                       (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Account created successfully!")
        UserLogin.destroy()
        import Search
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists.")
    finally:
        conn.close()


frame = ctk.CTkScrollableFrame(UserLogin)
frame.pack(pady=20, padx=60, fill="both", expand=True)

TheLabel = ctk.CTkLabel(frame, text="Hello to our SYTHMAR company!")
TheLabel.pack(pady=12, padx=10)

username_entry = ctk.CTkEntry(
    frame, placeholder_text="Username", corner_radius=12)
username_entry.pack(pady=6, padx=10)


password_entry = ctk.CTkEntry(frame, placeholder_text="Password",
                              show="*", corner_radius=12)
password_entry.pack(pady=12, padx=10)

button1 = ctk.CTkButton(frame, text="Login", command=login)
button1.pack(pady=6, padx=10)

button2 = ctk.CTkButton(
    frame, text="Create new account", command=create_account)
button2.pack(pady=6, padx=10)


def Checked():
    pass


checkBox = ctk.CTkCheckBox(
    frame, text="Remember the information for later?", command=Checked)
checkBox.pack(pady=12, padx=10)

UserLogin.mainloop()
