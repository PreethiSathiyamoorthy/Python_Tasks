numbers={}
n = int(input("Enter how many items:"))
for i in range(n):
    key=input("Enter the key:")
    value=int(input("Enter the value:"))
    numbers[key]=value
print("Dictionary:",numbers)
if numbers:
    print("The original dictionary is:",numbers)
    minimum=min(numbers.values())
    print("Minimum number in the dictionary:",minimum)
else:
    print("Dictionary is empty.no minimum value.")



