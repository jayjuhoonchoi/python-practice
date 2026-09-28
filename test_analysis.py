from database import get_connection, get_all_readings
from analysis import get_average, get_max

conn = get_connection()
df = get_all_readings(conn)

print("Average:", get_average(df))
print("Max:", get_max(df))