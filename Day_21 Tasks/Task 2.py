def add_student():
    name = input("enter the name :")
    mobile = input("enter the mobile number :")
    age = int(input("enter the age :"))
    mail = input("enter the mail :")
    file = open("H:\Free Python Class Preethi\Daily_Tasks_Preethi\Day_21 Tasks\File Handling\students.txt","a")
    file.write( f"name : {name}\n mobile : {mobile}\n age : {age}\n mail : {mail}\n")
    print("File is Create and written")

while True:
    choice = input("add student? enter yes or no :")
    if choice.lower() == 'yes':
        add_student()
    else:
        break
file.close()
print("added successfully")
