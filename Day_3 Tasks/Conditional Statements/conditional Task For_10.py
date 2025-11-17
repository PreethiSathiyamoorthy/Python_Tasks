held = int(input("Enter number of classess held :"))
attendent = int(input("Enter number of classess attendence :"))
percentage = (attendent/held)*100
if percentage<75:
    print("Not Allowed in sit Exam")
else:
    print("Allowed to Exam")
    
