try:
    a=int(input("Enter the a value:"))
    b=int(input("Enter the b value:"))
    c=a/b
    print(" A value is:",a)
    print(" B value is:",b)
    print(" C value is:",c)
except ZeroDivisionError:
    print("Cannot divide by zero Error")
except ValueError:
    print("Invalid value pls give me Integer Value")
else:
    print("Division result:",c)
finally:
    print("Code Execution is completed")
