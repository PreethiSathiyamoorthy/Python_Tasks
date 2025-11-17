fruits=["apple","orange","banana","cherry"]
fruits.pop()
print(fruits)


#method 2

my_list=[]
count = 0
n=int(input("how many elements do you want to be add to the list?"))
for i in range(n):
    element=input("Enter the elements")
    count=count+1
    my_list.append(element)
print("original list:",my_list)
if len(my_list)>0:
    my_list.pop()
    print("list after deleting last element:",my_list)
else:
    print("the list is empty,nothing to delete")
    
