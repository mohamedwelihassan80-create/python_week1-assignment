try:
    price = float(input("Enter the price of one item: "))
    quantity = int(input("Enter the quantity: "))

    total = price * quantity

    print(f"{quantity} items at Ksh{price:.2f} each = Ksh{total:.2f}")

except ValueError:
    print("Please enter numbers only.")