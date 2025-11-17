s=set()
string=''
n=int(input("Enter The no of elements:"))
for i in range(n):
      val=input("Enter the No:")
      s.add(val)
print(s)

for i in s:
    a=str(i)+","
    string+=a  #or string=string+a  
print("convert set into string:",string.split())
