import pandas as pd 


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


df = pd.read_csv('hydro_data.csv')
print(
    df.loc[1:1]
    )

def write_data():
    actual_date = EDate.get()
    with open("hydro_data1.csv", "a", newline="") as data_file:
        data_file.write(f"{actual_date}")
