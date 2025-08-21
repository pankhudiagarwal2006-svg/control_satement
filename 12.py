A = int(input("Enter angle A: "))
B = int(input("Enter angle B: "))
C = int(input("Enter angle C: "))

# Check if triangle is valid
if A + B + C == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")