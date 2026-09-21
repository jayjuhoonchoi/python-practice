import psycopg2

conn = psycopg2.connect(dbname="postgres", user="juhoon")
cursor = conn.cursor()

cursor.execute("SELECT * FROM readings")
rows = cursor.fetchall()

print(rows)

first_row = rows[0]
print(first_row[1])

import psycopg2
import random

conn = psycopg2.connect(dbname="postgres", user="juhoon")
cursor = conn.cursor()

def check_temperature(temp):
    if temp > 90:
        return "Warning"
    else:
        return "OK"

for i in range(3):
    temp = round(random.uniform(60,95), 1)
    status = check_temperature(temp)
    cursor.execute(
        "INSERT INTO readings (equipment_id, temperature, status) VALUES (%s, %s, %s)", ("NEW-DEVICE", temp, status)
    )

conn.commit()
print("Data saved")

