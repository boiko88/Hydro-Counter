import csv
from tkinter import *
from itertools import zip_longest
from tkcalendar import DateEntry


FONT_NAME = "Courier"

window = Tk()
window.title("Water Counter")
window.config(padx=10, pady=10)

fields = ["Hot", "Cold", "Electricity"]
info = ""


r = [f"{info}"]

# Date

EDate = DateEntry(width=11, background="blue",
                  foreground="white", font=FONT_NAME)
EDate.grid(column=3, row=3, sticky="w")

# Images

counter_image_hot = PhotoImage(file="images/water1.png")
canvas = Canvas(width=400, height=400)
canvas.create_image(200, 200, image=counter_image_hot)
canvas.grid(column=0, row=0, columnspan=3)

# Functions


def works():
    hot_water = []
    cold_water = []
    hydro = []
    data = [hot_water, cold_water, hydro]
    export_data = zip_longest(*data, fillvalue='')
    with open('counter_data.csv', 'w', encoding="ISO-8859-1", newline='') as file:
        write = csv.writer(file)
        actual_cold_water = cold_water_entry.get()
        hot_water.append(actual_cold_water)
        actual_hot_water = hot_water_entry.get()
        cold_water.append(actual_hot_water)
        actual_hydro = hydro_entry.get()
        hydro.append(actual_hydro)
        write.writerow(("hot water", "cold water", "hydro"))
        write.writerows(export_data)
        cold_water_entry.delete(0, END)
        hot_water_entry.delete(0, END)
        hydro_entry.delete(0, END)



# Test CSV Button

button2 = Button(text="Add Data",
                 width=12, command=works)
button2.grid(column=2, row=3)

# Entries

cold_water_entry = Entry(width=25)
cold_water_entry.grid(column=1, row=2)

hot_water_entry = Entry(width=25)
hot_water_entry.grid(column=2, row=2)

hydro_entry = Entry(width=25)
hydro_entry.grid(column=3, row=2)

# Label

hot_water_label = Label(text="Hot Water")
hot_water_label.grid(column=1, row=1)

cold_water_label = Label(text="Cold Water")
cold_water_label.grid(column=2, row=1)

hydro_label = Label(text="Hydro")
hydro_label.grid(column=3, row=1)


window.mainloop()
