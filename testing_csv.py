import pandas as pd 
import csv


# 1.  This function shows data from a specific row

# df = pd.read_csv('hydro_data.csv')
# print(
#     df.loc[1]
#     )

# 2. This data shows rows but from dictionaries
# hydro_data = {
#     "Hot Water Amount": [326],
#     "Cold Water Amount": [416],
#     "Hydro Amount": [18067],
# }


# df = pd.DataFrame(hydro_data, index = ["May", "June", "July"])
# print(
#     df.loc["May"]
#     )

# 3. Shall show a couple of rows and columns


# df = pd.read_csv('hydro_data.csv')
# print(
#     df.loc[1:1]
#     )

# def write_data():
#     actual_date = EDate.get()
#     with open("hydro_data1.csv", "a", newline="") as data_file:
#         data_file.write(f"{actual_date}")

# 4. Try to sort the data in different columns


# with open('output2.csv', newline='') as f_input:
#     csv_input = csv.reader(f_input, delimiter=';', quotechar='|')
#     header = next(csv_input)
#     rows = list(csv_input)

# with open('output2b.csv', 'w', newline='') as f_output:
#     csv_output = csv.writer(f_output, delimiter=';', quotechar='|')
#     csv_output.writerow(header)

#     for row in rows:
#         day, month, year = row[0].split('.')
#         row[1:4] = [day, month, year]
#         csv_output.writerow(row)


l1 = ['a', 'b', 'c', 'd', 'e']
l2 = ['f', 'g', 'i', 'j','k']
l3 = ['l', 'm', 'n', 'o', 'p']
l4 = ['q', 'r', 's', 't','u']
l5 = ['v', 'w', 'x', 'y', 'z']

r = zip(l1, l2, l3, l4, l5)

with open('Sample1.csv', "w") as s:
    w = csv.writer(s, delimiter="a")
    for row in r:
        w.writerow(row)
        
print("It Works")