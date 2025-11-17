my_set= {1,2,3,4,5,6,7,8,9,10}
size=len(my_set)
print("set:",my_set)
print("size of set:",size)

#method 2
s=[]
n=int(input("Enter The no of elements:"))
for i in range(n):
      val=(input("Enter the items:"))
      s.append(val)
      T=set(s)
      T=len(s)
print("size of  set:", T) 
