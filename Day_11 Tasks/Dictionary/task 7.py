d={}
num=int(input("enter the count:"))
for i in range(num):
    key=int(input("Enter the key:"))
    val=int(input("Enter the value:"))
    d[key]=val
print("dictionary:",d)
remove=int(input("Enter the key you want to remove:"))
r=d.pop(remove)
print("Remove items:",r)
print("After removing items dictionary:",d)
