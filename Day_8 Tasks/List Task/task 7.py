sub = []
count = 0
n=int(input("how many subjects do you want to be add to the list?"))

for i in range(n):
    subject=input("Enter the subject").strip()
    count=count+1
    sub.append(subject)
print("original list:",sub)
if len(sub)>0:
    print("list of subjects is :",sub)
else:
    print("the list is empty")



 #method 2

sub = []
for i in range(5):
    s=input("Enter the subject:").strip()
    sub.append(s)
print(sub)
