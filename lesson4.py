temperatures = [71.2, 68.9, 90.5, 55.0]

for temp in temperatures:
    if temp > 90:
        print("Warning: high temperature", temp)
    else:
        print("OK -", temp)


temperatures = []
temperatures.append(71.2)
temperatures.append(68.9)
temperatures.append(90.5)
print(temperatures)
print(len(temperatures))