try:
    a=input("Enter the a value:")
    b=int(input("Enter the b value:"))
    c=a+b
    print(" A value is:",a)
    print(" B value is:",b)
    print(" C value is:",c)
except ValueError:
    print("Invalid value pls give me Integer Value")
except TypeError:
    print("Invalid Data Type Pls Give Valid Data type")
else:
    print("Addition result:", c)
finally:
    print("Your Code Execution is complete")
    
