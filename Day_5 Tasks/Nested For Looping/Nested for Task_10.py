rows = int(input("Enter ur Number"))
for i in range(0, rows + 1):
    for j in range(0, i+1):
        print(chr(65 + j), end=" ")
    print()    
