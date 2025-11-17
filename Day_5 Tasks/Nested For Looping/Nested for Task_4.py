n=int(input("Enter the rows :"))
for i in range(n):
    for j in range(n):
        print("#", end=" ")
    print()

print("-----------------")
    
#method 2

n=int(input("Enter the no:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
    
