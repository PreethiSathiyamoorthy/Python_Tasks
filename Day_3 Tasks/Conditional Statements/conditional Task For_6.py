total_marks = int(input("Enter total marks (out of 400): "))
apptitude = int(input("Enter marks in Aptitude: "))
gd = int(input("Enter marks in GD: "))
technical = int(input("Enter marks in Technical: "))
hr = int(input("Enter marks in HR: "))

if 390<= total_marks <=400:
    salary = 30000
    eligible = True
elif 380<= apptitude <=390 and apptitude>=85:
    salary = 28000
    eligible = True
elif 370<= gd <=380 and gd>=90:
    salary = 25000
    eligible = True
elif 35<= Technical <=370 and Technical>=80:
    salary = 20000
    eligible = True
elif hr >= 95:
else:
    eligible = False
    print(" Your Nxt Round ")
if eligible:
    print("your eligible for addmision")
    print("offered salary:", salary)
else:
    print("your not eligible for addmision")
    
