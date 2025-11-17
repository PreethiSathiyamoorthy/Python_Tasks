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
#user input
name = input("Enter your name: ")
mail = input("Enter your mail: ")
address = input("Enter your address: ")
mobile = input("Enter your mobile: ")

#object create
obj=Education()
obj.info(name, mail, address, mobile)

# Educational details input
marks = []
n = int(input("\n Enter number of subjects: "))
for i in range(n):
    sub = input("Enter subject:")
    i=i+1            
    mark = int(input("Enter marks:",))
    marks.append(mark)

total = sum(marks)
percentage = total / n

# Call education info
obj.edu_info(marks, total, percentage)
