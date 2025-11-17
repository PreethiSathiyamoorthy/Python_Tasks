a = int(input(" Enter a a Value :"))
b = int(input(" Enter a b value :"))
print("Select operation :")
print(" 1. Add")
print(" 2. Subtraction")
print(" 3. Multiplication")
print(" 4. Division")

c = int(input(" Enter Your Operation:"))

if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
    print(a*b)
elif c == 4:
    print(a%b)
else:
    print("Give me a Valid Operation")
