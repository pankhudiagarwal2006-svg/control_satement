# Read two numbers
A = int(input("Enter number A: "))
B = int(input("Enter number B: "))

# Find maximum
if A > B:
    print("Maximum number is:", A)
elif B > A:
    print("Maximum number is:", B)
else:
    print("Both numbers are equal:", A)