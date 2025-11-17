try:
    List=[1,2,3,4,5,6,7]
    find=int(input("enter the value to find list have(1-7:"))
    if find in List:
        print("Value find",find)
    else:
        raise ValueError("Invalid value")
except Exception as e:
    print("error", e)
