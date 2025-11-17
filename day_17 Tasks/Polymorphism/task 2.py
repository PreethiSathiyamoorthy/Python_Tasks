class birds:
    def __init__(self,name):
        self.name = name
        print("i am",self.name)
    def make_sound(self):
        pass
class parrot(birds):
    def make_sound(self):
        return "Squawk"
class Sparrow(birds):
    def make_sound(self):
        return "Chrip"
a=input("Enter 1 bird name:")
b=input("Enter 2 bird name:")
obj2=parrot(a)
obj3=Sparrow(b)
print("parrot name is:",a,"makes sound",obj2.make_sound())
print("sparrow name is:",b,"makes sound",obj3.make_sound())

        
    
