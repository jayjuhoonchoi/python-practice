value = input("Enter pressure reading: ")


try:
    value = int(value)
    print("You entered:", value)
except ValueError:
    print("Invalid input. Please enter a number.")