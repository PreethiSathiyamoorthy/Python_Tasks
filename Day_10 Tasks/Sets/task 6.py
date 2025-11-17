a=input("Enter the elements for a list a:").split()
a = [int(num) for num in a]
b=input("Enter the elements for a list b:").split()
b = [int(num) for num in b]
set_a = set(a)
set_b = set(b)
differ = set_a - set_b #or differ = set_a.difference(set(b) used    
print("The above two list difference are:",differ)
combined = set_a| set_b
print("All elements:",combined)
