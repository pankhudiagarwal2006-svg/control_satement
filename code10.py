A = int(input("Enter A: "))
rev = 0
temp = A
while temp > 0:
    rev = rev*10 + temp%10
    temp //= 10
if rev == A:
    print("Yes, Palindrome")
else:
    print("No, Not Palindrome")