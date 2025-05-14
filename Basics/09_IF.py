age = int(input("Enter your age: "))

if age >= 18 and age < 120:
  print("You are eligible to vote.")
elif age < 0:
  print("Age cannot be negative.")
else:
  print("You aren't eligible to vote.")

