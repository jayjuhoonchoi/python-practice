import json

equipment = {"id": "CV-101", "temperature": 87.5, "status": "running"}

with open("equipment.json", "w") as file:
    json.dump(equipment, file)

print("JSON file created")

with open("equipment.json", "r") as file:
    data = json.load(file)

print(data)
print(data["temperature"])
print(type(data["temperature"]))


import random
import json
import csv

def check_temperature(temp):
    if temp > 90:
        return "Warning: high temperature"
    else:
        return "OK"

equipment_ids = ["CV-101", "PMP-07", "CV-102"]
readings = []

for eq_id in equipment_ids:
    temp = round(random.uniform(60, 95), 1)
    status = check_temperature(temp)
    readings.append({"id": eq_id, "temperature": temp, "status": status})

print("Readings:", readings)

with open("readings.json", "w") as file:
    json.dump(readings, file)

print("Saved to readings.json")


def check_vibration(vib):
    if vib > 8:
        return "Warning: high vibration"
    else:
        return "OK"

readings = []
values = [5.2, 9.1, 7.8]

for v in values:
    status = check_vibration(v)
    readings.append({"value": v, "status": status})

print(readings)