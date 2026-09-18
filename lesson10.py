from pathlib import Path

my_file = Path("readings.csv")
print(my_file)

folder = Path("data")
full_path = folder / "readings.csv"
print(full_path)
