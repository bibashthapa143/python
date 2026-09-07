# Example 1: print a formatted receipt from any items
def print_receipt(**items):
    total = 0
    for item, price in items.items():
        print(f"{item}: Rs.{price}")
        total += price
    print(f"Total: Rs.{total}")

print_receipt(apple=30, banana=20, mango=50)
