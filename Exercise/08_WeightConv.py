weight = float(input("Enter your weight:"))
unit = input("Killograms or Pounds? ( K / P ) :")

if unit == "k" or "K":
  weight = weight * 2.20462
  print(f"Your weight converted in pounds = {weight:.2f} lbs")
elif unit == "P" or "p":
  weight = weight / 2.20462
  print(f"Your weight converted in killograms = {weight:.2f} kg")
