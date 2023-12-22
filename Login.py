import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

UserLogin = ctk.CTk()
UserLogin.title("Login")
UserLogin.geometry("600x450")
UserLogin.iconbitmap('favicon.ico')
UserLogin.resizable(False, True)


def login():
    UserLogin.destroy()
    import Search


frame = ctk.CTkScrollableFrame(UserLogin)
frame.pack(pady=20, padx=60, fill="both", expand=True)

TheLabel = ctk.CTkLabel(frame, text="Hello to our SYTHMAR company!")
TheLabel.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(frame, placeholder_text="Username", corner_radius=12)
entry1.pack(pady=6, padx=10)


entry2 = ctk.CTkEntry(frame, placeholder_text="Password",
                      show="*", corner_radius=12)
entry2.pack(pady=12, padx=10)

button1 = ctk.CTkButton(frame, text="Login", command=login)
button1.pack(pady=6, padx=10)

button2 = ctk.CTkButton(frame, text="Create new account", command=login)
button2.pack(pady=6, padx=10)


def Checked():
    pass


checkBox = ctk.CTkCheckBox(
    frame, text="Remember the information for later?", command=Checked)
checkBox.pack(pady=12, padx=10)

UserLogin.mainloop()
