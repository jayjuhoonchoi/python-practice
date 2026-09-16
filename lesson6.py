equipment = {
    "id": "CV-101",
    "temperature": 87.5,
    "vibration": 4.2
}

print(equipment.get("id"))
print(equipment.get("temperature"))
print(equipment.get("status"))



equipment_list = [
    {"id": "CV-101", "temperature": 87.5},
    {"id": "PMP-07", "temperature": 91.3},
    {"id": "CV-102", "temperature": 66.5},
]

for eq in equipment_list:
    print(eq["id"], "-", eq["temperature"])



def check_temperature(temp):
    if temp > 90:
        return "Warning: high temperature"
    else:
        return "OK"

equipment_list = [
    {"id": "CV-101", "temperature": 87.5},
    {"id": "PMP-07", "temperature": 91.3},
    {"id": "CV-102", "temperature": 66.5},
]

for eq in equipment_list:
    status = check_temperature(eq["temperature"])
    print(eq["id"], "-", status)