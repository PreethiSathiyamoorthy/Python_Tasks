def addition(**a):
    for i,j in a.items():
        print("key",i,"value is ",j)
addition(a=20,b=40,c="preethi",d=23)

#method 2

def addition(**a):
    for i, j in a.items():
        print("key", i,"value",j)
def user_input_addition():
    a=int(input("enter value for a:"))
    b=int(input("enter value for b:"))
    c=int(input("enter value for c:"))
    d=int(input("enter value for d:"))
    addition(a=a,b=b,c=c,d=d)
user_input_addition()    
        
