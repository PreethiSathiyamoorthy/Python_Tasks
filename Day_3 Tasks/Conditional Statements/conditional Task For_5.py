year = int(input("Enter your year (1-3): "))
semester = int(input("Enter your semester (1-2): "))

if year == 1 and Semester== 1:
    print("Subjects:")
    print("1. English")
    print("2. Mathematics I")
    print("3. Physics")
    print("4. Chemistry")
    print("5. Programming in C")

elif year == 1 and semester == 2:
    print("Subjects:")
    print("1. Mathematics II")
    print("2. Environmental Science")
    print("3. Computer Organization")
    print("4. Data Structures")
    print("5. Digital Logic")

elif year == 2 and semester == 1:
    print("Subjects:")
    print("1. Object Oriented Programming")
    print("2. Database Management System")
    print("3. Operating Systems")
    print("4. Computer Networks")
    print("5. Software Engineering")

elif year == 2 and semester == 2:
    print("Subjects:")
    print("1. Design and Analysis of Algorithms")
    print("2. Microprocessor")
    print("3. Web Technology")
    print("4. Computer Graphics")
    print("5. Java Programming")

elif year == 3 and semester == 1:
    print("Subjects:")
    print("1. Artificial Intelligence")
    print("2. Machine Learning")
    print("3. Cloud Computing")
    print("4. Compiler Design")
    print("5. Internet of Things")

elif year== 3 and semester == 2:
    print("Subjects:")
    print("1. Data Science")
    print("2. Mobile Application Development")
    print("3. Cyber Security")
    print("4. Blockchain Technology")
    print("5. Project Work")
    
else:
    print("Invalid input! Please enter correct year and semester.")
