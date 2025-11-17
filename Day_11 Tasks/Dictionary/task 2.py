d={}
num=int(input("enter the count:"))
for i in range(num):
    key=input("Enter the key:")
    val=input("Enter the value:")
    d[key]=val
print("dictionary:",d)
for key,val in d.items():
    print(key,d[key])
                    
