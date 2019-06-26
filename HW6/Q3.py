def TDT():
    h = input ("what is the initial height?:\n")
    q = input("what is the bounciness?:\n")
    n = input("what is the number of bounces?:\n")
    ans=h+h*q*((1-(q**(n-1)))*2/(1-q))+h*(q**n)
    return ans
              
                                   
          
   
   
