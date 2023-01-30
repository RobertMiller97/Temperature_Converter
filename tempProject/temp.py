# Temperature Converter

unit = input("Celsius or Fahrenheit:  ")

temp = float(input("Enter temperature:  "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp} C")

elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp} C")
else:
    print(f"unit id invalid")
