def Digit_Counter(num):
    counter=0
    
    while num>0:
        mod = num%10
        num = num/10
        if mod ==1:
            counter += 1
        else: continue    
        
    
    return counter