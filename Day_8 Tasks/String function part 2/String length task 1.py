#method 1
text = input("Enter the string:")
len_text = len(text)
print("the length of the string is:",len_text)


#method 2

text = input("Enter the string:")
count =0
for char in text:
    count=count+1
print("the length of the string is:", count)    
