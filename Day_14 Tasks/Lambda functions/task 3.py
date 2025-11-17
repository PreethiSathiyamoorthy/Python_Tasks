import math
numbers =[2,4,6,8,10,12]
print(numbers)
n=int(input("Enter number to multiply:"))
result = [math.prod([num,n]) for num in numbers]
print("result list:", result)



#method 2 without math method
numbers=[1,2,3,4,5]

print(numbers)
n=int(input("Enter a number to multiply:"))
result=[]
for i in numbers:
    result.append(i*n)
print("result list:",result)   
