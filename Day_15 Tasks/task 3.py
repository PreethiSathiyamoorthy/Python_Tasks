class calculation:
    def add (self,a,b):
        return a+b
    def sub (self, a,b):
        return a-b
    def mul (self, a,b):
        return a*b
    def div (self, a,b):
        if b==0:
            return "Error:cannot divide by zero"
        return a/b
    

#user from Input
print("Enter the first value (A):")
a=int(input())
print("Enter the Second Value (B):")
b=int(input())

#object create
obj=calculation()
print("\n---Calculation---")
print("A=(a), B=(b)")
print("addition:",obj.add(a,b))
print("Subtraction:",obj.sub(a,b))
print("Multiplication:",obj.mul(a,b))
print("Division:",obj.div(a,b))

