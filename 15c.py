# Read percentage from user
percentage = float(input("Enter your percentage: "))

# Check grade
if percentage < 25:
    print("Grade: D")
elif percentage <= 45:
    print("Grade: C")
elif percentage <= 65:
    print("Grade: B")
elif percentage <= 85:
    print("Grade: A")
else:
    print("Grade: A+")