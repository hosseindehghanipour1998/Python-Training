
def GCD(a,b):
    
    if a%b ==0:
        return b
    else:
        return GCD(a,a%b)



m=input("Enter the 1st number:\n")
n=input("Enter the 2nd number:\n")
result=GCD(m,n)
print result
