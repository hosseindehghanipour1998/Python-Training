
a = input ("1st No?:\n")
b = input ("2nd No?:\n")
#GCD calculator
def GCD(a,b):
    if a>=b:
        if a%b==0:
            return b
        else:
            return GCD(a,a%b)
    if b>=a:
        if b%a==0:
            return a
        else:
            return GCD(b,b%a)

print GCD(a,b),"is the GCD"
#LCM calculator
#a*b//GCD = LCM
LCM = (a*b)/GCD(a,b)
print LCM,"is the LCM"

