order_amount = float(input("Enter the order amount: ")) # Example order amount :150

def apply_discount(order_amount):
    if order_amount > 100:
        return order_amount * 0.9
    return order_amount

final_price = apply_discount(order_amount)

print(f"Final price after applying discount: ${final_price:.2f}")
