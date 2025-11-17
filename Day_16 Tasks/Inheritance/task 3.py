class School:
    def information(self, name, mail, mobile, address):
        self.name = name
        self.mail = mail
        self.mobile = mobile
        self.address = address
        print("\n--- School Information ---")
        print(f"Name: {self.name}")
        print(f"Mail: {self.mail}")
        print(f"Mobile: {self.mobile}")
        print(f"Address: {self.address}")

class Staff(School):
    def staffInformation(self, name, mail, mobile, address, dept):
        self.information(name, mail, mobile, address)
        print(f"Department: {dept}")


class Student(School):
    def studentInformation(self, name, mail, mobile, address, dept):
        self.information(name, mail, mobile, address)
        print(f"Department: {dept}")


#Main Program
choice = input("Are you a Student, Staff or School? ").lower()

if choice == "student":
    s = Student()
    s.studentInformation("Arun", "arun@gmail.com", "9876543210", "Chennai", "Computer Science")

elif choice == "staff":
    st = Staff()
    st.staffInformation("Priya", "priya@gmail.com", "9123456780", "Madurai", "Mathematics")

elif choice == "school":
    sc = School()
    sc.information("ABC Matric School", "abcschool@gmail.com", "9000090000", "Coimbatore")

else:
    print("Invalid choice! Please enter Student, Staff or School.")
