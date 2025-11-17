text="skysky"
vowels="aeiou AEIOU"
count = 0
for char in text:
    if char in vowels:
         count=count+1
    print("Number of vowels:", count)
