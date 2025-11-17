L=[1,2,3]
for i in range(4,7):
    L.append(i)
print(L)


#method 2

my_list=[1,2,3]
add_list=[4,5,6]
my_list.extend(add_list)
print(my_list)

#method 3

numbers = [1,2,3]
new_numbers = [4,5,6]
for num in new_numbers:
    numbers.append(num)
    print(numbers)
    
