d={}
num=int(input("enter the count:"))
for i in range(num):
    key=input("Enter the key:")
    val=input("Enter the value:")
    d[key]=val
print("dictionary:",d)
key=input("enter the key values:")
if key in d:
    print("given key is exist")
else:
    print("given key is not exist")
