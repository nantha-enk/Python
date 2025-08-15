temperature = float(input("Enter temperature:"))
unit = (input("Enter unit (C for cesius or F for fahrenheit):"))
if unit.upper() == "C":
    temperature = (temperature * 9/5) + 32
elif unit.upper() == "F":
    temperature = (temperature - 32) * 5/9
print("Converted temperature:",temperature)