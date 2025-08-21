A = int(input("Enter number A: "))
B = int(input("Enter number B: "))
C = int(input("Enter number C: "))

# Find minimum
if A <= B and A <= C:
    print("Minimum number is:", A)
elif B <= A and B <= C:
    print("Minimum number is:", B)
else:
    print("Minimum number is:", C)