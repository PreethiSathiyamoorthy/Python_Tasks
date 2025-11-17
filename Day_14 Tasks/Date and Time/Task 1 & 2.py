# 1st part - datetime fields
from datetime import datetime as d
x = d.now()

y = x.timetuple()
print("time type :\n", y)
print("time tuple year :", y[0])
print("month of year :", y[1])
print("week number of year :", x.strftime("%U"))
print("day of the week :", x.strftime("%w"))
print("day of year :", x.strftime("%j"))
print("day of the month :", y[2])
print("day of week :", y[6])

print("---------------------------------------------------------------")

# 2nd part - leap year checker
def leapyear(y):
    if y % 4 != 0:
        return False
    elif y % 100 != 0:
        return True
    elif y % 400 != 0:
        return False
    else:
        return True

year = int(input("enter the year :"))
if leapyear(year):
    print("It is leap year ")
else:
    print("it is not leap year ")
print("---------------------------------------------------------------")



