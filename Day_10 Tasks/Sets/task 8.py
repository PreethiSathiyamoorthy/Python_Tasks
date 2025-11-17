#method 1 for user gives a strings
numbers = input("Enter the items :").split()
num_set = set(numbers)
print("original list:",numbers)
print("converted set:", num_set)

#method 2 for user gives a numbers
numbers = input("Enter the items :").split()
numbers = [int(num) for num in numbers]
num_set = set(numbers)
print("original list:",numbers)
print("converted set:", num_set)
