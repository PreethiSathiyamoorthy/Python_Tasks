'''names=[]
while True:
    name = input("Enter a name(type 'stop' to end):").strip()
    if name.lower()=="stop":
        break
    names.append(name)
    print("names entered:",names)'''
#2 method

name=[]
for i in range(5):
    n=input("enter the name:")
    name.append(n)

    if i=='stop':
        break
print(name)    
    
