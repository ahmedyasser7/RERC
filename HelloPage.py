from PIL import Image
import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

Hello = ctk.CTk()
Hello.title("HelloPage")
Hello.geometry("600x450")
Hello.iconbitmap('favicon.ico')
Hello.resizable(False, True)

frame = ctk.CTkFrame(Hello)
frame.pack(fill="both", expand=True)


my_image = ctk.CTkImage(dark_image=Image.open(
    "wallpaperflare.com_wallpaper.jpg"), size=(500, 350))

image_label = ctk.CTkLabel(frame, image=my_image, text="")
image_label.pack()


def owner():
    Hello.destroy()
    import LoginOwner


def tenant():
    Hello.destroy()
    import Choose


button1 = ctk.CTkButton(frame, text="Owner", command=owner)
button1.pack(pady=10, padx=10)

button2 = ctk.CTkButton(frame, text="Tenant", command=tenant)
button2.pack(pady=10, padx=10)

Hello.mainloop()
