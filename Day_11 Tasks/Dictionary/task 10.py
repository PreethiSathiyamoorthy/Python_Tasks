d={}
num=int(input("Enter the count:"))
for i in range(num):
    key=input("Enter the key:")
    val=input("Enter the value:")
    d[key]=val
print("dictionary:",d)
key=d.keys()
print("keys:",key)
