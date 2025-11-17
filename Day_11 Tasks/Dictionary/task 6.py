d={}
num=int(input("enter the count:"))
for i in range(num):
    key=int(input("Enter the key:"))
    val=int(input("Enter the value:"))
    d[key]=val
print("dictionary:",d)
product=1
for value in d.values():
    product=product*value
print("Multiply:",product)    
