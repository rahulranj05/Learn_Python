num = float(input("Enter a number:"))
num2 = float(input("Enter another number:"))

opp = input("What is the operation you want to perform? ( + , - , * , / ) :")

if opp == "+":
  print(num + num2)
elif opp == "-":
  print(num - num2)
elif opp == "*":
  print(num * num2)
elif opp == "/":
  if num2 != 0:
    print(round((num / num2),2))
  else:
    print("Error! Division by zero is not allowed.")