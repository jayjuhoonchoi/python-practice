import random

temperatures = []

for i  in range(5):
    reading = round(random.uniform(60,95), 1)
    temperatures.append(reading)

print("All readings:", temperatures)

for temp in temperatures:
    if temp > 90:
        print("Warning: high temperature -", temp)
    else:
        print("OK -", temp)
