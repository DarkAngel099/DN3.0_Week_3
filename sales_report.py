sales = [200, 600, 150, 800, 300]

def generate_report(sales):
    for sale in sales:
        if sale > 500:
            print(f"Sale: ${sale} - **High Sale**")
        else:
            print(f"Sale: ${sale}")

generate_report(sales)

total_sales = sum(sales)
print(f"Total sales for the month: ${total_sales}")
