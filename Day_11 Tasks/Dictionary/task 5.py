d={}
num=int(input("enter the count:"))
for i in range(num):
    key=int(input("Enter the key:"))
    val=int(input("Enter the value:"))
    d[key]=val
print("dictionary:",d)
key=int(input("enter the key values:"))
sum_of_values=sum(d.values())
print("sum of key valuea:",sum_of_values)
