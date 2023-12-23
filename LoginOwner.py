import customtkinter as ctk
import tkinter as tk
import sqlite3


# def connect_db():
#     conn = sqlite3.connect('')
#     return conn


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

OwnerLogin = ctk.CTk()
OwnerLogin.title("LoginOwner")
OwnerLogin.geometry("600x450")
OwnerLogin.iconbitmap('favicon.ico')
OwnerLogin.resizable(False, True)


def login():
    #     username = entry1.get()
    #     password = entry2.get()

    #     conn = connect_db()
    #     cursor = conn.cursor()

    #     cursor.execute(
    #         "SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    #     result = cursor.fetchone()

    #     if result is None:
    #         messagebox.showerror("Error", "Invalid username or password.")
    #     else:
    #         messagebox.showinfo("Success", "Logged in successfully!")

    #     conn.close()
    OwnerLogin.destroy()
    import Owner


frame = ctk.CTkScrollableFrame(OwnerLogin)
frame.pack(pady=20, padx=60, fill="both", expand=True)

TheLabel = ctk.CTkLabel(frame, text="Hello our Partner!")
TheLabel.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(frame, placeholder_text="ID")
entry1.pack(pady=12, padx=10)


entry2 = ctk.CTkEntry(frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button1 = ctk.CTkButton(frame, text="Login", command=login)
button1.pack(pady=12, padx=10)

checkBox = ctk.CTkCheckBox(frame, text="Stay Signed?")
checkBox.pack(pady=12, padx=10)

OwnerLogin.mainloop()
