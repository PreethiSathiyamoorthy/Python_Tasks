try:
    a=input("Enter the first number:")
    b=input("Enter the second number:")
    if a.isdigit() and b.isdigit():
        print(int(a),int(b))
    else:
        raise TypeError("if the input is not a numerical!pls Enter Valid  Data type!")
except Exception as e :
    print("error",e)
                        
