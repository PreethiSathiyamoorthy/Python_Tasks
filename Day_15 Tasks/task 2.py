from datetime import date, datetime
#To create a Class fiest
class person:
#To create a method    
    def _init_(self, Name, Country, dob):
        self.Name = Name
        self.Country = Country
        self.dob =datetime.strptime(dob, '%y-%m-%d').date()
    def age(self):
        today = date.today()
        age = today.year - self.dob. year
        if(today.month, today.day)<(self.DOB.month, self.dob.day):
            age=age-1
            return age
#input from user        
print("\n---Person Details Input:----")
name=input("Enter Your Name:")
Country=input("Enter Your Country:")
dob=input("Enter Your date of birth(YYYY-MM-DD):")

#To create a object
obj = person(name, Country, dob)

print("\n---Person Output---")
print("name:",obj.name(name))
print("country:",obj.country(country))
print("DOB:",obj.dob(dob))
print("age:",obj.age(age))      
      
      

      
    
