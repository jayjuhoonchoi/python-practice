import pandas as pd

df = pd.read_csv("readings.csv")
print(df)

average = df["temperature"].mean()
print(average)

print(df["temperature"].max())
print(df["temperature"].min())

hot = df[df["temperature"] > 90]
print(hot)
