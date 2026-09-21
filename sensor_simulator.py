import random
import json
from pathlib import Path
from datetime import datetime

def check_temperature(temp):
    if temp > 90:
        return "Warning: high temperature"
    else:
        return "OK"

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

temperatures = []

for i in range(5):
    reading = round(random.uniform(60, 95), 1)
    temperatures.append(reading)

print("All readings:", temperatures)

results = []

for temp in temperatures:
    status = check_temperature(temp)
    print(status, "-", temp)
    results.append({
        "temperature": temp,
        "status": status,
        "timestamp": get_timestamp()
    })

output_path = data_folder / "sensor_results.json"

with open(output_path, "w") as file:
    json.dump(results, file)

print("Saved results to:", output_path)



