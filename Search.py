import customtkinter as ctk
import tkinter as tk
import sqlite3


def connect_db():
    conn = sqlite3.connect('')
    return conn


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

Search = ctk.CTk()
Search.geometry("800x600")
Search.title("SYTHMAR")
Search.iconbitmap('favicon.ico')
Search.resizable(False, True)

frame = ctk.CTkScrollableFrame(Search)
frame.pack(pady=20, padx=60, fill="both", expand=True)


TheMainLabel = ctk.CTkLabel(
    frame, text="Let's search Together for your prefrences!", bg_color='#0a0908')
TheMainLabel.pack(pady=12, padx=10)

# def combobox_call1(choice):
#     print("You choosed", choice)

# combobox_type = ctk.CTkComboBox(frame, values=["Sale", "Rent"], command=combobox_call1)
# combobox_type.set("Rent")
# combobox_type.pack(pady= 12, padx= 10)

List1 = []

com2 = ctk.CTkLabel(frame, text="Choose the type of the estate",
                    bg_color='#22333b', width=20)
com2.pack()


def combobox_call2(choice):
    print("The estate is: ", choice)
    List1.append(choice)


combobox_estate = ctk.CTkComboBox(frame, values=[
                                  "Villa", "Apartment", "House", "Office", "Co-working space", "Room"], command=combobox_call2)
combobox_estate.set("Room")
combobox_estate.pack(pady=12, padx=10)

com3 = ctk.CTkLabel(
    frame, text="Choose the area of the estate", bg_color='#22333b')
com3.pack()


def combobox_call3(choice):
    print("The area is: ", choice)
    List1.append(choice)


combobox_area = ctk.CTkComboBox(
    frame, values=["50", "100", "150", "200", "250", "300"], command=combobox_call3)
combobox_area.set("50")
combobox_area.pack(pady=12, padx=10)

com4 = ctk.CTkLabel(
    frame, text="Choose the maximum price you need", bg_color='#22333b')
com4.pack()


def combobox_call4(choice):
    print("The price is: ", choice)
    List1.append(choice)


combobox_price = ctk.CTkComboBox(frame, values=[
                                 "500", "1000", "5000", "10,000", "50,000", "100,000", "500,000", "1,000,000"], command=combobox_call4)
combobox_price.set("500")
combobox_price.pack(pady=12, padx=10)

com5 = ctk.CTkLabel(
    frame, text="Choose the maximum number of rooms", bg_color='#22333b')
com5.pack()


def combobox_call5(choice):
    print("The number of rooms is: ", choice)
    List1.append(choice)


combobox_room = ctk.CTkComboBox(
    frame, values=["1", "2", "3", "4", "5", "6"], command=combobox_call5)
combobox_room.set("1")
combobox_room.pack(pady=12, padx=10)


def search():
    Search.destroy()
    import ShowingResults


button1 = ctk.CTkButton(frame, text="Search", command=search)
button1.pack(pady=12, padx=10)

Search.mainloop()
