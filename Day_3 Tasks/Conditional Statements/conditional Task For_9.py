salary = float(input("enter employes salary:"))
years_of_service = int(input("enter years of service"))
if years_of_service>5:
    bonus=salary*0.05
    print("eligible for bonus")

    totalsalary=salary+bonus
    print("total salary including bonus:",totalsalary)
else:
        bonus=0
        print("No bonus, service is less than equal to 5 years:"
              )
        
