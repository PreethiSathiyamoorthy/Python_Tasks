a=input("Enter the elements for a list a,separated by spaces:").split()
a = [int(num) for num in a]
b=input("Enter the elements for a list b,separated by spaces:").split()
b = [int(num) for num in b]
c=input("Enter the elements for a list c,separated by spaces:").split()
c = [int(num) for num in c]
set_a = set(a)
set_b = set(b)
set_c = set(c)
common = set_a & set_b & set_c
print("Common elements:",common)
combined = set_a| set_b | set_c
print("All elements:",combined)


#method 2

a={1,2,3}
b={4,5,2}
c={6,7,2}
common = a.intersection(b,c)
print("Common elements in three sets is :", common)

