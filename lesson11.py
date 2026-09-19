import os

home = os.environ.get("HOME")
print(home)


secret = os.environ.get("MY_SECRET")
print(secret)

missing = os.environ.get("NOT_SET_YET", "default_value")
print(missing)

