# Get marks from the user
n = int(input("Enter your marks: "))

# Check the marks and print the result
if n >= 80:
    print("Excellent")
elif n >= 60:
    print("Good")
elif n >= 40:
    print("Pass")
else:
    print("Fail")
