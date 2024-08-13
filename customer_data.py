customer_data = {'Emma': 120, 'John': 75, 'Sophia': 90}

def update_purchase(customer_data, name, amount):
    if name in customer_data:
        customer_data[name] = amount
    else:
        print(f"Customer {name} not found.")

update_purchase(customer_data, 'John', 100)

print(customer_data)
