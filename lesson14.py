from datetime import datetime

now = datetime.now()
print(now)

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

reading = {
    "temperature": 87.5,
    "status": "OK",
    "timestamp": get_timestamp()
}

print(reading)