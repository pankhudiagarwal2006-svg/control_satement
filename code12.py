A = int(input("Enter A: "))
B = int(input("Enter B: "))
res = 1
for i in range(B):
    res *= A
print("A^B=",res)