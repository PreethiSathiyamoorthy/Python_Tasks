s=[]
n=int(input("Enter The no of elements:"))
for i in range(n):
      val=int(input("Enter the No:"))
      s.append(val)
      T=set(s)
print("Original value",T)

r=int(input("What do you Want Remove:"))    
u=T.remove(r)
print("Remove set is:", T) 
