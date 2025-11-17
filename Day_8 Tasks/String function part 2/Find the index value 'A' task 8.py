text = input("Enter the string:")
position = text.index('a')
print("The index of first 'a'is:",position)



#Method 2

text = input("Enter a string:")
if 'a' in text:
    position=text.index('a')
    print("The Index of first 'a' is:", position)
else:
    print("'a' not found in string")
