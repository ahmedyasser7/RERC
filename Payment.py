import customtkinter as ctk
import tkinter as tk
import numpy as np
import sqlite3


def connect_db():
    conn = sqlite3.connect('')
    return conn


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

Payment = ctk.CTk()
Payment.title("Payment")
Payment.geometry("600x450")
Payment.iconbitmap('favicon.ico')
Payment.resizable(False, True)

frame = ctk.CTkScrollableFrame(Payment)
frame.pack(pady=20, padx=60, fill="both", expand=True)

entry1 = ctk.CTkEntry(
    frame, width=160, placeholder_text="Your Name", corner_radius=15)
entry1.pack(pady=6, padx=10)

entry2 = ctk.CTkEntry(
    frame, width=160, placeholder_text="Your Phone number", corner_radius=15)
entry2.pack(pady=6, padx=10)

entry3 = ctk.CTkEntry(
    frame, width=160, placeholder_text="Your National ID", corner_radius=15)
entry3.pack(pady=6, padx=10)

entry4 = ctk.CTkEntry(
    frame, width=160, placeholder_text="Your visa card number", show="*", corner_radius=15)
entry4.pack(pady=6, padx=10)


def Pay():
    Payment.destroy()
    import SuccessfulOperation


button1 = ctk.CTkButton(frame, text="Pay", command=Pay, corner_radius=35)
button1.pack(pady=20, padx=10)


Payment.mainloop()
