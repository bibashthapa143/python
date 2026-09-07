# Example 1: multiply all numbers passed
def multiply(*numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

print(multiply(2, 3, 4))   # 24
print(multiply(5))         # 5
print(multiply())          # 1 (empty args, nothing to multiply)
