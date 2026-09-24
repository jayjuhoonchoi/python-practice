import random
import logging
import psycopg2
import pandas as pd
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def check_temperature(temp):
    if temp > 90:
        return "Warning"
    else:
        return "OK"

conn = psycopg2.connect(dbname="postgres", user="juhoon")
cursor = conn.cursor()
logging.info("Starting sensor check")

temperature = []

for i in range(5):
    reading = round(random.uniform(60,95), 1)
    temperature.append(reading)

for temp in temperature:
    status = check_temperature(temp)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if status == "Warning":
        logging.warning(f"High temperature detected: {temp}")

    cursor.execute(
    "INSERT INTO readings (equipment_id, temperature, status) VALUES (%s, %s, %s)", ("AUTO-CHECK", temp, status)
    )

conn.commit()
logging.info("All readingvs saved to database")
df = pd.read_sql("SELECT * FROM readings", conn)

print(df["temperature"].mean())
print(df["temperature"].max())

