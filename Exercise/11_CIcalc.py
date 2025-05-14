principle = 0
time = 0
rate = 0

principle = int(input("Enter the principle amount: "))
time = float(input("Enter the time in years: "))
rate = float(input("Enter the rate of interest: "))

CI = principle * ( 1 + ( rate / 100))**time

print(f"The amount after compound intrest is : {CI:.2f}")