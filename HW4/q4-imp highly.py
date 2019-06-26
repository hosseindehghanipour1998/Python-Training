a = input("what?:\n")
sum1 = 0
sum2 = 0
mod2 = 0
mod = 0

while (a!=0):
    mod = a%10
    a = a//10
    sum1 = sum1 + mod
print sum1
if sum1<10 :
     print "the answer is correct"
elif sum1>=10:
    while (sum1>=10):
        while(sum1!=0):
                mod2 = sum1 %10
                sum1 = sum1 //10
                sum2 = sum2 +  mod2
                
                
        sum1 = sum2
        print sum1
        sum2=0
        
       
        
                
            
   
