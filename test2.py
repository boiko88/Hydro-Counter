import csv
from tkinter import *
from itertools import zip_longest
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter.ttk import Notebook
 



FONT_NAME = "Courier"

# UI

window = Tk()
window.title("Water Counter")
window.config(padx=10, pady=10)

# 2 different frames

Tab = Notebook(window)

F1 = Frame(Tab, width=500, height=500)
F2 = Frame(Tab, width=500, height=500)

Tab.add(F1, text="Water and Hydro")
Tab.add(F2, text="Actual Prices")
Tab.grid(column=0, row=0)

fields = ["Hot", "Cold", "Electricity"]
info = ""

hot_water = []
cold_water = []
hydro = []


r = [f"{info}"]

# Date

EDate = DateEntry(F1, width=11, background="blue",
                  foreground="white", font=FONT_NAME)
EDate.grid(column=3, row=3, sticky="w")

# Images

counter_image_hot = PhotoImage(file="images/water1.png")
canvas = Canvas(F1, width=400, height=400)
canvas.create_image(200, 200, image=counter_image_hot)
canvas.grid(column=1, row=0, columnspan=3)

# Functions


def clean_entries():
    cold_water_entry.delete(0, END)
    hot_water_entry.delete(0, END)
    hydro_entry.delete(0, END)


def works():
    data = [hot_water, cold_water, hydro]
    export_data = zip_longest(*data, fillvalue='')
    actual_cold_water = cold_water_entry.get()
    actual_hot_water = hot_water_entry.get()
    actual_hydro = hydro_entry.get()
    if actual_cold_water == "" or actual_hydro == "" or actual_hot_water == "":
        messagebox.showinfo("Empty Entry Error", "Some entries are empty")
    else:
        with open('counter_data.csv', 'w', encoding="ISO-8859-1", newline='') as file:
            write = csv.writer(file)
            hot_water.append(actual_cold_water)
            cold_water.append(actual_hot_water)
            hydro.append(actual_hydro)
            write.writerow(("hot water", "cold water", "hydro"))
            write.writerows(export_data)
            clean_entries()


# Test CSV Button

button2 = Button(F1, text="Add Data",
                 width=12, command=works)
button2.grid(column=4, row=3)

# Entries

cold_water_entry = Entry(F1, width=25)
cold_water_entry.grid(column=2, row=2)

hot_water_entry = Entry(F1, width=25)
hot_water_entry.grid(column=3, row=2)

hydro_entry = Entry(F1, width=25)
hydro_entry.grid(column=4, row=2)

# Label

hot_water_label = Label(F1, text="Hot Water")
hot_water_label.grid(column=2, row=1)

cold_water_label = Label(F1, text="Cold Water")
cold_water_label.grid(column=3, row=1)

hydro_label = Label(F1, text="Hydro")
hydro_label.grid(column=4, row=1)


window.mainloop()
