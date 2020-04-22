a = input("chi nazarete?\n")
base = input("what base?:\n")
b = 0
n = 0
while a >= 10**(n):
    n = n+1
print n
#print n ro inja vase in gozashtam ke bbinm tavan ro dorost mohasebe mikone ya na
while n>= 0:
    
    e = a//10**(n-1)
    
    c = e * (base**(n-1))
    b = b + c
    a = a%10**(n-1)
    n = n - 1
print b
