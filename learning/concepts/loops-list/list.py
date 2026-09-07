fruits=["apple","banana","mango"]
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # mango

fruits[1]="orange" #change the value of fruits[1]
print(f"after changing value of {fruits[1]}:",fruits)

fruits.append("grape")
fruits.remove("apple")
print(f"after removing the {fruits[0]}: {fruits} and adding {fruits[2]}" )

print(f"Total numbers of items in list: {len(fruits)}")

# append()   → add
# remove()   → remove by value
# pop()      → remove by index
# sort()     → sort
# reverse()  → reverse 
# len()      → number of items
fruits.reverse()

print(fruits)

