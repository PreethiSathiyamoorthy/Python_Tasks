text = input("Enter the String:")
all_alpha = text.isalpha()
print(all_alpha)


#method 2

text = input("Enter the string:")
if text.isalpha():
    print("All Characters are alphabets.")
else:
    print("All Characters arev not alphabets.")


#method 3(Without isalpha()function)

text = input("Enter the string:")
all_alpha = True
for char in text:
    if not('A'<= char <='Z' or 'a'<=char <='z'):
        all_alpha = false
        break
if all_alpha:
    print("All Characters are alphabets.")
else:
    print("All Characters arev not alphabets.")
