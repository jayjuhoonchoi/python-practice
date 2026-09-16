import random

def check_temperature(temp):
    if temp > 90:
        return "Warning: high temperature"
    else:
        return "OK"

temperatures = []

for i  in range(5):
    reading = round(random.uniform(60,95), 1)
    temperatures.append(reading)

print("All readings:", temperatures)

for temp in temperatures:
    status = check_temperature(temp)
    print(status, "-", temp)
