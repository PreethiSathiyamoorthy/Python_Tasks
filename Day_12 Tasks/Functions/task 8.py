def palindrome(s):
    L=s.lower()
    rev=L[::-1]
    if L==rev:
        print("passed string is palindrome")
    else:
        print("passes string is not palindrome")
st=input("Enter the string:")
palindrome(st)
