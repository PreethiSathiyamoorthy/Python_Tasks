# 3rd
from datetime import datetime as d

x = "12 January,2002"
print("date :", d.strptime(x, "%d %B,%Y"))

print("--------------------------------------------")

# 4th
from datetime import datetime as d

x = d.now().time()
print("current time :", x)

print("--------------------------------------------")

# 5th
from datetime import datetime as d

string = "July 1 14 2:43PM"
print("convert datetime :", d.strptime(string, "%B %d %y %I:%M%p"))

print("--------------------------------------------")

# 6th
from datetime import datetime as d, timedelta

x = d.now()
z = x - timedelta(5)
z = x - timedelta(days=5)
print("current day :", x)
print("5 days before :", z)

print("--------------------------------------------")
