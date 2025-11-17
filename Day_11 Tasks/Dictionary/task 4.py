d={}
d1={}
num=int(input("enter the count:"))
for i in range(num):
    key=input("Enter the key:")
    val=input("Enter the value:")
    d[key]=val
print("dictionary:",d)
num1=int(input("enter the count:"))
for j in range(num):
    key1=input("Enter the key1:")
    val2=input("Enter the value1:")
    d1[key1]=val2
print("dictionary:",d1)
update=d.update(d1)
print("merge 2 dictionary:",d)
