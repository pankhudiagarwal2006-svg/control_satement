# Read year from user
year = int(input("Enter a year: "))

# Leap year check
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is Not a Leap Year.")