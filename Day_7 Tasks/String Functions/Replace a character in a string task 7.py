original = "The Quick brown dog jumps over the lazy dog"
new_string = original.replace("d", "f")
print(new_string)


#method 2

original = input("Enter the original String:")
char_to_replace = input("Enter the character you want to replace:")
new_char = input("Enter the new character:")
new_string = original.replace(char_to_replace, new_char)
print("The new string is:", new_string)
                              
