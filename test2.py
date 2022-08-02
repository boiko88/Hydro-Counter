import csv
from tkinter import *
from itertools import zip_longest

window = Tk()
window.title("Water Counter")
window.config(padx=10, pady=10)

fields = ["Hot","Cold", "Electricity"]
info = ""


r = [f"{info}"]


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

