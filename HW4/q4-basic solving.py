a = input("what?:\n")
sum2=0 
sum3=0 
sum1 = 0
mod = 0
mod3 = 0
mod2=0


while (a!=0):
    mod = a%10
    a = a//10
    sum1 = sum1 + mod
print "sum:",sum1
   
if (sum1 <10):
    print sum1,"\t is the answer"
elif (sum1>=10):
    sum2 = sum1 //10
    mod2 = sum1 %10
    sum2 = sum2 +  mod2
print "sum2:",sum2
if sum2>=10:
    sum3 = sum2 //10
    mod3 = sum2 %10
    sum3 = sum3 +  mod3
print "sum3:",sum3
    
    
    
