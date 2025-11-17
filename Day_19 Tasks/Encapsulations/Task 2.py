class employee:
    def __init__(self,name):
        self.__name=name
        self.__salary =0
     def set_salary(self,amount):
         if amount>0:
             self.__salary=amount
         else:
             return("Invalid salary:)
     def get_salary(self):
         return self.__salary
     def get_name(self):
         return self.__name
emp = emplotee("Preethi")
emp.set_salary(10000)
print(emp.get_salary())
print(emp.get_name())
