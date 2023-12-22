import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

OwnerLogin = ctk.CTk()
OwnerLogin.title("LoginOwner")
OwnerLogin.geometry("600x450")
OwnerLogin.iconbitmap('favicon.ico')
OwnerLogin.resizable(False, True)

# Need to be edited.


def login():
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
