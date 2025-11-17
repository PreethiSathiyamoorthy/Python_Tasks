# 15th part - age calculate

from datetime import date

def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year
    # subtract 1 if birthday hasn't occurred yet this year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age

dob = date(2002, 1, 12)
print("age:", calculate_age(dob))
print("-----------------------------------------------------------------")

# 7th
from datetime import datetime as d, timedelta

x = d.now()
yesterday = x - timedelta(1)
tomorrow = x + timedelta(1)

print("Yesterday :", yesterday)
print("Today     :", x)
print("Tomorrow  :", tomorrow)

print("------------------------------------------------------------")

# 8th
from datetime import datetime as d, timedelta

x = d.strptime("28:33.0", "%M:%S.%f")
add = x + timedelta(seconds=5)
print(add.strftime("%M:%S.%f")[:8])

print("------------------------------------------------------------")

# 9th
from datetime import datetime as d

x = d.now()
print("Current :", x)
print("In milliseconds :", x.timestamp())

print("------------------------------------------------------------")

# 10th
from datetime import datetime as d

x = d.strptime("2015,6,16", "%Y,%m,%d")
print("Week number :", x.strftime("%U"))
    
