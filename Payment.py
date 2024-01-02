import customtkinter as ctk
import tkinter as tk
import numpy as np
from tkinter import messagebox
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
    frame, width=170, placeholder_text="Your Name", corner_radius=15)
entry1.pack(pady=7, padx=10)

entry2 = ctk.CTkEntry(
    frame, width=170, placeholder_text="Your Phone number", corner_radius=15)
entry2.pack(pady=7, padx=10)

entry3 = ctk.CTkEntry(
    frame, width=170, placeholder_text="Your National ID", corner_radius=15)
entry3.pack(pady=7, padx=10)

entry4 = ctk.CTkEntry(
    frame, width=170, placeholder_text="Your visa card number", show="*", corner_radius=15)
entry4.pack(pady=7, padx=10)

entry5 = ctk.CTkEntry(
    frame, width=170, placeholder_text="Your visa card password", show="*", corner_radius=15)
entry5.pack(pady=7, padx=10)


def Pay():
    if entry1.get() == "" or entry2.get() == "" or entry3.get() == "" or entry4.get() == "":
        messagebox.showerror("Error", "please fill all the entries")
        return
    if len(entry2.get()) != 11:
        messagebox.showwarning("Wait", "Phone number is not valid!")
        return
    if len(entry3.get()) != 14:
        messagebox.showwarning("Wait", "National ID is not valid!")
        return
    if len(entry4.get()) != 16:
        messagebox.showwarning("Wait", "Visa number is not valid!")
        return
    if len(entry5.get()) != 4:
        messagebox.showwarning("Wait", "Visa password is not valid!")
        return
    Payment.destroy()
    import SuccessfulOperation


button1 = ctk.CTkButton(frame, text="Pay", command=Pay, corner_radius=20)
button1.pack(pady=20, padx=10)


Payment.mainloop()
