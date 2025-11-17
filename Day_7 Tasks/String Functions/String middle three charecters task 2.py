def middle_three(s):
    n = len(s)
    if n<3 or n%2==0:
        return"String must be odd length and at least 3 characters"
    mid=n//2
    return s[mid-1: mid+2]
s="Preethi"
print(middle_three(s))
