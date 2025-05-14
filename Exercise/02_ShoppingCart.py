item = input("Enter the item you want to buy: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))

total_cost = price * quantity

print(f"You bought {quantity} {item}(s) at ${price} each. \nTotal cost: ${total_cost}.")
