for f in range(1, 11, 2):   # (Start, stop, step)
    print(f)

# Print numbers from 1 to 4
for f in range(1, 5):
    print(f)

print("================")

# Print numbers using while loop
count = 0
while count < 5:
    print(count)
    count += 1

print("=================")

# Use break and continue
for i in range(1, 10):
    if i == 5:
        break
    elif i % 2 == 0:
        print(i)
        continue

