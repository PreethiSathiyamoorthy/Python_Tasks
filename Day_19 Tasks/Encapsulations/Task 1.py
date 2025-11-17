class Student:
    def __init__(self, name):
        self.__name = name        # private variable
        self.__grades = []        # private variable

    def add_grade(self, grade):
        self.__grades.append(grade)

    def get_average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def get_name(self):
        return self.__name
    
student1 = Student("Preethi")

# add grades
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(95)
student1.add_grade(95)
student1.add_grade(95)


# display name and average

print("Student Name:", student1.get_name())
print("Average Marks:", student1.get_average())
print()

#another method 2

class Student:
    def __init__(self, name):
        # private variables
        self.__name = name
        self.__grades = []

    # method to add a grade
    def add_grade(self, grade):
        self.__grades.append(grade)

    # method to calculate average grade
    def get_average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)

    # method to get student name
    def get_name(self):
        return self.__name

# get name from user
name = input("Enter student name: ")

# create object
student1 = Student(name)

# get number of subjects
count = int(input("Enter number of subjects: "))

# get grades from user
for i in range(count):
    grade = input("Enter the subject name:")
    grade = int(input("Enter mark for subject:"))
    i=i+1
    student1.add_grade(grade)

# display result
print("\n--- Student Report ---")
print("Name:", student1.get_name())
print("Average Marks:", student1.get_average())
