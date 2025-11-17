username = input("Enter Your User Name :")
gmail = input("Enter Your Email :")
if len(username)>2:
    print("username is Valid")
else:
    print("username is not Valid")
if "@" in gmail and "."in gmail:
    print("gmail ID is Valid")
else:
    print("gmail ID is not Valid")
    
