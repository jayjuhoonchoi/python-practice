with open("log.txt", "w") as file:
    file.write("Sensor check complete\n")
    file.write("All readings normal\n")


print("Done writing to file")


with open("log.txt", "a") as file:
    file.write("New entry added\n")
    