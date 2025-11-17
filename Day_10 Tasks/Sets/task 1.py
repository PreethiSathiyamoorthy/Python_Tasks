#method 1
items=[1,2,3,4,5,6,7,7,6]
my_set = set(items)
print("original list:",items)
print("created set:",my_set)

#method 2
item={1,2,3,4,5,6,6,8}
print("created set:",item)


#method 3

s=[]
n=int(input("Enter The no of elements:"))
for i in range(n):
      val=int(input("Enter the No:"))
      s.append(val)
      T=set(s)
print("Create set:", T)      
      
