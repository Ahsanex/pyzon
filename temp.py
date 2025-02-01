temp = float(input("Enter the temp value: "))
unit_from = input("Enter the unit in which your temperature is in: ")
unit_to = input("Enter the unit in which you want your temperature: ")

if unit_from == "C" and unit_to == "F":
    temp = (temp * 9/5) + 32
    print("CONVERTED TEMPERATURE IS: " + str(temp) + " F")

elif unit_from == "F" and unit_to == "C":
    temp = (temp - 32) * 5/9
    print("CONVERTED TEMPERATURE IS: " + str(temp) + " C")

elif unit_from == "C" and unit_to == "K":
    temp = temp + 273.15
    print("CONVERTED TEMPERATURE IS: " + str(temp) + " K")

elif unit_from == "K" and unit_to == "C":
    temp = temp - 273.15
    print("CONVERTED TEMPERATURE IS: " + str(temp) + " C")

elif unit_from == "F" and unit_to == "K":
    temp = (temp - 32) * 5/9 + 273.15
    print("CONVERTED TEMPERATURE IS: " + str(temp) + " K")

elif unit_from == "K" and unit_to == "F":
    temp = (temp - 273.15) * 9/5 + 32
    print("CONVERTED TEMPERATURE IS: " + str(temp) + " F")

else:
    print("Error: Invalid unit conversion")
