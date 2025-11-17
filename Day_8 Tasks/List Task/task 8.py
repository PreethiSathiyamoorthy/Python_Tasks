L=["preethi","dinesh","prasanna","renu","2"]
print(L)
R=input("Enter what do you want remove specific item:")
L.remove(R)
print(L)


#method 2

mylist=["Apple","Banana","Orange","Pineapple"]
print(mylist)
remove_item=input("Enter what do you want remove specific item:").strip()
if remove_item in mylist:
  mylist.remove(remove_item)
  print("Updated list:", mylist)
else:
    print("items not found in the list")

