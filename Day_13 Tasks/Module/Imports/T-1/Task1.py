def prime(n):
    if n<=1:
        return "not prime"
    for i in range(2,n):
        if n%i==0:
            return "not prime"
        else:
            return "prime"
    


def perfect(n):
    if n<=1:
        return False  
    total = 0
    for i in range(1,n):
        if n%i==0:
            total=total+i
            
    if total==n:
        return True  
    else:
        return False  
    
def amstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == n

   

    
    
        
        
