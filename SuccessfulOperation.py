from PIL import Image
import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

Success = ctk.CTk()
Success.title("Successful")
Success.geometry("600x450")
Success.iconbitmap('favicon.ico')
Success.resizable(False, True)

frame = ctk.CTkScrollableFrame(Success)
frame.pack(pady=20, padx=60, fill="both", expand=True)

Tap = ctk.CTkTabview(frame, corner_radius=20, fg_color="#22333b")

t1 = Tap.add("Submitted")
t2 = Tap.add("Done")

my_image = ctk.CTkImage(dark_image=Image.open(
    "comic (59).jpg"), size=(350, 250))

image_label = ctk.CTkLabel(t1, image=my_image, text="")


def Done():
    print('Done')
    Success.destroy()


TheLabel = ctk.CTkLabel(
    t1, text="Thanks for using our system \nWe wait for your second entry!\n\n\nGo to Done Page to Close the system!")


button1 = ctk.CTkButton(t2, text="Done", command=Done)
Tap.pack(pady=10)
image_label.pack()
TheLabel.pack(pady=12, padx=10)
button1.pack(pady=10, padx=10)


Success.mainloop()
