my_set={1,2,3,4,5,6,7,8,9,10}
print("original set:",my_set)
my_tuple=tuple(my_set)
print("set converted into tuple:",my_tuple)
my_tuple_2=(1,2,3,4,5,6,7,8,9,10)
print("original tuple:",my_tuple_2)
my_set2=set(my_tuple_2)
print("Tuple converted into set:", my_set2)


#method 2
s=[]
n=int(input("Enter The no of elements:"))
for i in range(n):
      val=int(input("Enter the No:"))
      s.append(val)
print(s)
print("convert set into tuple:",tuple(s))
print("convert tuple into set:",set(s))
