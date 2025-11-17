words = ["preethi","dinesh","prasanna","praveen","apple","school"]
length_six = []
for w in words:
    if len(w) == 6:
       length_six.append(w)
print("words with length 6:",length_six)



#method 2

words=[]
word_count=0
s=input("Enter the how many items do you want in count:")
n=input("Enter the items:")
for w in (n):
    if len(w)==6:
        words.append(w)       
        print("Words with length 6:",words)
    else:
        print("not found")
        
    
