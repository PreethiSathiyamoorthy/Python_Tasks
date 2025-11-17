#11th
from datetime import datetime as d
x = d(2001, 2, 28)
y = d(2000, 2, 28)
z = x - y
print("between days :", z)

print("--------------------------------------------------")

#12th
from datetime import datetime as d
d1 = d(2022, 1, 1, 0, 0, 0)
d2 = d(2022, 1, 2, 12, 30, 30)

diff = d2 - d1

print("Difference :", diff.days, "days", diff.seconds // 3600, "hours",
      (diff.seconds // 60) % 60, "minutes", diff.seconds % 60, "seconds")

print("--------------------------------------------------")
