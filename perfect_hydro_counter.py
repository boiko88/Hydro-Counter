from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter.ttk import Notebook
import pandas as pd
import csv

FONT_NAME = "Courier"


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Water Counter")
window.config(padx=10, pady=10)


# Tabs

Tab = Notebook(window)

F1 = Frame(Tab, width=500, height=500)
F2 = Frame(Tab, width=500, height=500)

Tab.add(F1, text="Water and Hydro")
Tab.add(F2, text="Actual Prices")
Tab.grid(column=0, row=2)

# Images

counter_image_hot = PhotoImage(file="images/water1.png")
canvas = Canvas(F1, width=400, height=400)
canvas.create_image(200, 200, image=counter_image_hot)
canvas.grid(column=0, row=1, columnspan=3)

def empty_data_error():
    pass


def add_all_consumed_data():

    count_cold_water = cold_water_entry.get()
    count_hot_water = hot_water_entry.get()
    count_hydro = hydro_entry.get()
    actual_date = EDate.get()

    with open("water.txt", "a") as data_file:
        data_file.write(
            f" The actual cold water count is {count_cold_water}, for hot water it is {count_hot_water}, for hydro it is {count_hydro} and the actual date is {actual_date}\n")
        cold_water_entry.delete(0, END)
        hot_water_entry.delete(0, END)
        hydro_entry.delete(0, END)
    
    dataset = pd.read_csv("hydro_data.csv")

    data = dataset.iloc[0:1].values
    with open("hydro_data1.csv", "a", newline="") as data_file:
        data_file.write(f"{count_hydro}\n")
        print(data_file)
        
def write_data():
    actual_date = EDate.get()
    with open("hydro_data1.csv", "a", newline="") as data_file:
        data_file.write(f"{actual_date}")
        cold_water_entry.delete(0, END)
        hot_water_entry.delete(0, END)
        hydro_entry.delete(0, END)


# Test CSV Button 

test_csv_button = Button(F1, text="CSV Test",
                        width=12, command=write_data)
test_csv_button.grid(column=2, row=4)

# Hot Water

hot_water_label = Label(F1, text="Hot Water")
hot_water_label.grid(column=0, row=2)

hot_water_entry = Entry(F1, width=25)
hot_water_entry.grid(column=1, row=2)


# Cold Water

cold_water_label = Label(F1, text="Cold Water")
cold_water_label.grid(column=0, row=3)

cold_water_entry = Entry(F1, width=25)
cold_water_entry.grid(column=1, row=3)

cold_water_add = Button(F1, text="Add all Data",
                        width=12, command=add_all_consumed_data)
cold_water_add.grid(column=2, row=3)

# Hydro

hydro_label = Label(F1, text="Hydro")
hydro_label.grid(column=0, row=4)

hydro_entry = Entry(F1, width=25)
hydro_entry.grid(column=1, row=4)

# Date


EDate = DateEntry(F1, width=11, background="blue",
                  foreground="white", font=FONT_NAME)
EDate.grid(column=4, row=3, sticky="w")

EDate = DateEntry(F1, width=11, background="blue",
                  foreground="white", font=FONT_NAME)
EDate.grid(column=4, row=3, sticky="w")


# Prices F2 tab 

hot_water_price_label = Label(F2, text=f"Hot water price is 211 rubles per M3. You have consumed so your total for hot water is" )
hot_water_price_label.grid(column=0, row=2)



window.mainloop()
