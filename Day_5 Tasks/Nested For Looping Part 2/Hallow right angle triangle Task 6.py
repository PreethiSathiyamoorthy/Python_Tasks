n=int(input("Enter the no of rows"))
for i in range(0, n+1):
    for j in range(0,i+1):
        if j==0 or j==i or i==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()           
