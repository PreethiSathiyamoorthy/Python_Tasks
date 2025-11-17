def count_char(s):
    vowels=0
    consonants=0
    special=0
    for i in s:
        if i.isalpha():
            if i in 'aeiouAEIOU':
                vowels+=1
            else:
                consonants+=1
        elif not i.isspace():
            special+=1
    print("vowels:",vowels,"consonants:",consonants)
get = input("Enter the string :")
count_char(get)
                
