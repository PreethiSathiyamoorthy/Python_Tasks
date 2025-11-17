text = input("Enter a string:")
result = ""
for char in text:
    if not char.isdigit():
       result=result+char
print("string without digits:",result)    
