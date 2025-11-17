def print_even_numbers(*args):
    print("Even numbers are:")
    for num in args:
        if num % 2 == 0:
            print(num, end=' ')
    print()
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(n) for n in numbers] #each strings convert an integers
print_even_numbers(*numbers)
