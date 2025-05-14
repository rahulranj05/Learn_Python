import math

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))

hyp = math.sqrt(pow(side1, 2) + pow(side2, 2))

print(f"The length of the hypotenuse is: {round(hyp, 2)} cm")