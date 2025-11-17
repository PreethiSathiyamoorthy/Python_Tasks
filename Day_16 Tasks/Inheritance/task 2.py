class Personal:
    def info(self, name, mail, address, mobile):
        print("\n---- Personal Information ----")
        print("Name:", name)
        print("Mail:", mail)
        print("Address:", address)
        print("Mobile:", mobile)

class Education(Personal):
    def edu_info(self, marks, total, percentage):
        print("\n---- Educational Information ----")
        print("Marks of each subject:", marks)
        print("Total:", total)
        print("Percentage:", percentage , "%")

class Bank(Education):
    def bank_info(self, acc_num, bank_name, branch, ifsc, balance):
        print("\n---- Bank Information ----")
        print("Account Number:", acc_num)
        print("Bank Name:", bank_name)
        print("Branch:", branch)
        print("IFSC Code:", ifsc)
        print("Available Balance:", balance)

# Create object
obj = Bank()

name = input("Enter your name: ")
mail = input("Enter your mail: ")
address = input("Enter your address: ")
mobile = input("Enter your mobile: ")

marks = []
n = int(input("\n Enter number of subjects: "))
for i in range(n):
    sub = input("Enter subject:")
    i=i+1            
    mark = int(input("Enter marks:",))
    marks.append(mark)
total = sum(marks)
percentage = total / n

acc_num = input("\n Enter your Account Number: ")
bank_name = input("Enter Bank Name: ")
branch = input("Enter Branch Name: ")
ifsc = input("Enter IFSC Code: ")
balance = input("Enter Available Balance: ")

obj.info(name, mail, address, mobile)
obj.edu_info(marks, total, percentage)
obj.bank_info(acc_num, bank_name, branch, ifsc, balance)
