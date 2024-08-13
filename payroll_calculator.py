hours_worked = float(input("Enter the number of hours worked: "))# Example: 40 hours worked
hourly_rate = float(input("Enter the hourly rate: "))# Example: $15 per hour

def calculate_pay(hours, rate):
    return hours * rate

total_pay = calculate_pay(hours_worked, hourly_rate)

print(f"Total pay for the employee: ${total_pay:.2f}")
