import csv
import os

file_name = "save.csv"
fieldnames = ["Name", "Location", "Time"]


data_list = [
    {"Name": "David", "Location": "Kirinyaga", "Time": "10:00pm"},
    {"Name": "John", "Location": "Kirinyaga", "Time": "9:30pm"},
    {"Name": "Mary", "Location": "Nairobi", "Time": "8:45pm"},
    {"Name": "Paul", "Location": "Mombasa", "Time": "11:00pm"},
    {"Name": "Jane", "Location": "Eldoret", "Time": "7:15pm"},
    {"Name": "Alice", "Location": "Nairobi", "Time": "6:50pm"},
    {"Name": "Mike", "Location": "Nakuru", "Time": "5:30pm"}
]

file_exists = os.path.exists(file_name)


with open(file_name, "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    
    if not file_exists or os.stat(file_name).st_size == 0:
        writer.writeheader()

   
    writer.writerows(data_list)

print("Data successfully added")
