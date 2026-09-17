import csv

equipment_list = [
    {"id": "CV-101", "temperature": 87.5},
    {"id": "PMP-07", "temperature": 91.3},
    {"id": "CV-102", "temperature": 66.5},
]

with open("readings.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "temperature"])
    writer.writeheader()
    for eq in equipment_list:
        writer.writerow(eq)

print("CSV file created")


with open("readings.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

def check_temperature(temp):
    if temp > 90:
        return "Warning: high temperature"
    else:
        return "OK"

with open("readings.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        status = check_temperature(float(row["temperature"]))
        print(row["id"], "-", status)
