def check_temperature(temp):
    if temp > 90:
        return "Warning: high temperature"
    else:
        return "OK"

result1 = check_temperature(95)
result2 = check_temperature(70)

print(result1)
print(result2)


def check_temperature(temp):
    temp = 999
    if temp > 90:
        return "Warning: high temperature"
    else:
        return "OK"

original_temp = 50
result = check_temperature(original_temp)
print("Function result:", result)
print("Original temp is still:", original_temp)