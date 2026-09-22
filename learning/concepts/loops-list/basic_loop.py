# Print odd numbers from 1 to 9
for f in range(1, 11, 2):
    print(f)

# Print numbers from 1 to 4
for f in range(1, 5):
    print(f)

print("================")

# Print numbers from 0 to 4
count = 0
while count < 5:
    print(count)
    count += 1

print("=================")

# Print even numbers until 5 is reached
for i in range(1, 10):
    if i == 5:
        break
    elif i % 2 == 0:
        print(i)
        continue
