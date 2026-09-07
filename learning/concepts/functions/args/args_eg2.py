# Example 2: find the biggest number, any count
def find_max(*numbers):
    if not numbers:
        return None
    return max(numbers)

print(find_max(3, 7, 2))       # 7
print(find_max(10))            # 10
