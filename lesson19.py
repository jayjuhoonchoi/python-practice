values = [3.2, 8.5, 6.1, 9.0]
for index, v in enumerate(values):
    device_name = f"CV-0{index + 1}"
    print(device_name,":", v)

    if v > 8:
        print("Warning: excessive vibration")

import pandas as pd
df = pd.DataFrame({"values": [3.2, 8.5, 6.1, 9.0]})
print(df["values"].mean())


print("올바른 예시)

import pandas as pd

values = [3.2, 8.5, 6.1, 9.0]

for index, v in enumerate(values):
    device_name = f"CV-0{index + 1}"
    print(device_name, ":", v)

    if v > 8:
        print("Warning: excessive vibration")

df = pd.DataFrame({"values": values})
print(df["values"].mean())