from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter.ttk import Notebook

FONT_NAME = "Courier"


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Water Counter")
window.config(padx=10, pady = 10)


# Tabs

Tab = Notebook(window)

F1 = Frame(Tab, width = 500, height = 500)
F2 = Frame(Tab, width=500, height=500)
F3 = Frame(Tab, width=500, height=500)

Tab.add(F1, text="Hot Water")
Tab.add(F2, text="Cold Water")
Tab.add(F3, text="Hydro")

Tab.grid(column = 0, row = 2)


# Pictures 

counter_image_hot = PhotoImage(file="images/water1.png")
canvas = Canvas(F1, width=400, height=400)
canvas.create_image(200, 200, image=counter_image_hot)
canvas.grid(column=0, row = 1, columnspan=3)

counter_image_cold = PhotoImage(file="images/water2.png")
canvas = Canvas(F2, width=400, height=400)
canvas.create_image(200, 200, image=counter_image_cold)
canvas.grid(column=0, row = 1, columnspan=3)

counter_image_hydro = PhotoImage(file="images/hydro.png")
canvas = Canvas(F3, width=500, height=500)
canvas.create_image(250, 250, image=counter_image_hydro)
canvas.grid(column=0, row = 1, columnspan=3)

# Functions 

def add_consumed_amount_cold_water():

    count = cold_water_entry.get()
    actual_date = EDate.get()

    with open ("water.txt", "a") as data_file:
        data_file.write(f" The actual water count is {count} for cold water and the actual date is {actual_date}\n")
        cold_water_entry.delete(0,END)


def add_consumed_amount_hot_water():

    count = hot_water_entry.get()
    actual_date = EDate.get()

    with open ("water.txt", "a") as data_file:
        data_file.write(f" The actual water count is {count} for hot water and the actual date is {actual_date}\n")
        hot_water_entry.delete(0,END)


def add_consumed_amount_hydro():

    countT1 = hydro_entry.get()
    countT2 = hydro_entry.get()
    countT3 = hydro_entry.get()
    actual_date = EDate.get()

    with open ("water.txt", "a") as data_file:
        data_file.write(f" The actual electricity count is {countT1} and the actual date is {actual_date}\n")
        hydro_entry.delete(0,END)
        hydro_entry.delete(0,END)
        hydro_entry.delete(0,END)

# Hot Water

hot_water_label = Label(F1, text = "Hot Water")
hot_water_label.grid(column = 0, row = 2)

hot_water_entry = Entry(F1, width = 25)
hot_water_entry.grid(column = 1, row = 2)

hot_water_add = Button(F1, text = "Add hot water", width = 12, command=add_consumed_amount_hot_water)
hot_water_add.grid(column = 2, row = 2)


# Cold Water

cold_water_label = Label(F2, text = "Cold Water")
cold_water_label.grid(column = 0, row = 2)

cold_water_entry = Entry(F2, width = 25)
cold_water_entry.grid(column = 1, row = 2)

cold_water_add = Button(F2, text = "Add cold water", width = 12, command=add_consumed_amount_cold_water)
cold_water_add.grid(column = 2, row=2)

# Hydro

hydro_label = Label(F3, text = "Hydro")
hydro_label.grid(column = 0, row = 2)

hydro_entry = Entry(F3, width = 25)
hydro_entry.grid(column = 1, row = 2)

hydro_add = Button(F3, text = "Add Hydro", width = 12, command=add_consumed_amount_hydro)
hydro_add.grid(column = 2, row=2)

# Date


EDate = DateEntry(F1, width = 11, background ="blue", foreground = "white", font=FONT_NAME)
EDate.grid(column=1, row=3, sticky="w" )

EDate = DateEntry(F2, width = 11, background ="blue", foreground = "white", font=FONT_NAME)
EDate.grid(column=1, row=3, sticky="w" )


window.mainloop() 
