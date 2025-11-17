#method 1
a=[1,2,3,4]
b=[4,6,6,7]
set_a=set(a)
set_b=set(b)
common = set_a.intersection (set_b)
print("Common elements:",common)
combined = set_a|set_b
print("All elements:", combined)

#method 2

a=[2,4,6,8]
b=[1,2,3,4]
set_a=set(a)
set_b=set(b)
common = set_a & set_b
print("Common elements:",common)
combined = set_a|set_b
print("All elements:", combined)

#method 3
a=input("Enter the elements for a list a,separated by spaces:").split()
a = [int(num) for num in a]
b=input("Enter the elements for a list b,separated by spaces:").split()
b = [int(num) for num in b]
set_a = set(a)
set_b = set(b)
common = set_a & set_b
print("Common elements:",common)
combined = set_a| set_b
print("All elements:",combined)

