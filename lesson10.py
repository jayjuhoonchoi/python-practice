from pathlib import Path

my_file = Path("readings.csv")
print(my_file)

folder = Path("data")
full_path = folder / "readings.csv"
print(full_path)


full_path = Path("data") / "logs" / "readings.csv"
print(full_path)

from pathlib import Path

folder = Path("data")
folder.mkdir(exist_ok=True)
print("Folder ready:", folder)
