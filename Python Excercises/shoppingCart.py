item = input("What item would you like to buy?: ")
price = float(input("What price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}")
print(f"The price for the {item} is £{total}")