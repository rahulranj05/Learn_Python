temp = float(input("Enter temperature: "))
unit = input("Enter unit (C / F) : ")

if unit == "C" or "c":
  f = (temp * 9/5) + 32
  print(f"{temp}°C is equal to {f}°F")
elif unit =="F" or "f":
  c = (temp - 32) * 5/9
  print(f"{temp}°F is equal to {c}°C")