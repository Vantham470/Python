# Python file detection

import os

file_path = "C:/Users/DELL/Desktop/test"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print("That location doesn't exist")


# Python writing file (.txt, .json, .csv)

# 1. txt file writing
employees = ["Nita", "Levin", "Vanntham"]
text_data = "I love Nita!"

# file_path = "output.txt"
file_path = "C:/Users/DELL/Desktop/output.txt" # to generate the file within the same folder

# with open(file=file_path, mode="w") as file: "w = Write file"
# # with open(file_path, "w") as file: "a = Append"
# with open(file=file_path, mode="x") as file: "x = create"
try:
    with open(file_path, "a") as file: # w = write a file
       for employee in employees:
           file.write(employee + "\n")
       print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exist!")

# 2. json file writing
import json
employee = {
    "name": "Nita",
    "age": 17,
    "job": "Accounting"
}

file_path = "C:/Users/DELL/Desktop/output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4) # indent = add key value and number of key value is space
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

# 3. csv file writing
import json
import csv
employees = [["name", "age", "job"],
            ["Levin", 18, "Web Developer"],
            ["Nita", 17, "Cyber Security"],
            ["Vanntham", 19, "Software Developer"]]

file_path = "C:/Users/DELL/Desktop/output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

# Python reading file (.txt, .json, .csv)

# txt file reading
file_path = "C:/Users/DELL/Desktop/input.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to read this file")

# Json file reading
import json

file_path = "C:/Users/DELL/Desktop/input.txt"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You have no permission to read that file")

# csv file reading

import csv

file_path = "C:/Users/DELL/Desktop/input.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file) # give a memory address
        for line in content:
            print(line[0]) # output =  name 
            print(line[1]) #           age
            print(line[3]) #           job
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You have no permission to read that file")

