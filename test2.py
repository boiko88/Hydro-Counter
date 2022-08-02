from email.quoprimime import quote
import hashlib
import csv
from tkinter import *
from itertools import zip_longest

window = Tk()
window.title("Water Counter")
window.config(padx=10, pady=10)

fields = ["Hot","Cold", "Electricity"]
info = ""


r = [f"{info}"]

def write_data():
    with open('data.csv', "w", newline="") as f:
        info = cold_water_entry.get()
        writer = csv.writer(f, delimiter=",")
        writer.writerow(fields)
        for i in info:
            writer.writerow(i)
            cold_water_entry.delete(0, END)

def write_list_csv():
    with open('data_new.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(fields)
        w = csv.writer(f, delimiter=' ',)
        for row in r:
            row = cold_water_entry.get()
            w.writerow(row)
            cold_water_entry.delete(0, END)
        for row in r:
            row = hot_water_entry.get()
            w.writerow(row)
            hot_water_entry.delete(0, END)   
        for row in r:
            row = hydro_entry.get()
            w.writerow(row)
            hydro_entry.delete(0, END)

def works():
    hot_water = []
    cold_water = []
    hydro = []
    data = [hot_water, cold_water, hydro]
    export_data = zip_longest(*data, fillvalue = '')
    with open('item_zip.csv', 'w', encoding="ISO-8859-1", newline='') as file:
        write = csv.writer(file)
        actual_cold_water = cold_water_entry.get()
        hot_water.append(actual_cold_water)
        actual_hot_water = hot_water_entry.get()
        cold_water.append(actual_hot_water)
        actual_hydro = hydro_entry.get()
        hydro.append(actual_hydro)
        write.writerow(("hot water", "cold water", "hydro"))
        write.writerows(export_data)
        print(export_data)                
    

# Test CSV Button 


# button = Button(text="Test",
#                         width=12, command=write_list_csv)
# button.grid(column=1, row=2)

button2 = Button(text="Test CSV",
                        width=12, command=works)
button2.grid(column=2, row=3)

# Entries

cold_water_entry = Entry(width=25)
cold_water_entry.grid(column=1, row=1)

hot_water_entry = Entry(width=25)
hot_water_entry.grid(column=2, row=1)

hydro_entry = Entry(width=25)
hydro_entry.grid(column=3, row=1)

# Label 

hot_water_label = Label(text="Hot Water")
hot_water_label.grid(column=1, row=0)

cold_water_label = Label(text="Cold Water")
cold_water_label.grid(column=2, row=0)

hydro_label = Label(text="Hydro")
hydro_label.grid(column=3, row=0)

            
window.mainloop()

