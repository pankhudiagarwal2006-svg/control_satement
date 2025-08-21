a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

# Check if it's a valid triangle
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    # Right Triangle
    if a == 90 or b == 90 or c == 90:
        print("Right Triangle")
    # Obtuse Triangle
    elif a > 90 or b > 90 or c > 90:
        print("Obtuse Triangle")
    # Acute Triangle
    else:
        print("Acute Triangle")
else:
    print("Not a valid triangle")
