'''Q1'''
def nice(input1):
    i = 1
    counter = 0
    while i<=input1:
        mod1 = input1%i
        if mod1 ==0:
            a = i
            if a%2!=0:
                counter = counter +1
            elif a%2==0:
                counter = counter
        i+=1
    if counter %2==0:
        return True
    else:
        return False

###########################
                
''' Q2'''


def NNR():
    i = 0
    while i<2:
        input1 = input("chi nazarete?:\t")
    
        
        function = nice(input1)
        if function ==True:
            
            return input1

##############################################
''' Q3'''
def function(input2):
    
    counter = 1
    sum1 = 0
    while counter <= input2:
        num1 =(counter)*((-1)**counter)
        sum1 = sum1 + num1
        counter+=1
    return abs(sum1)*input2



##################################################
'''q4'''
def f(num):
    counter=0
    
    while num>0:
        mod = num%10
        num = num/10
        if mod ==1:
            counter += 1
        else: continue    
        
    
    return counter

##################################################
''' q5'''
print f(function(NNR()))
'''
nnr = NNR()
function1 = function(nnr)
f1 = f(function1)
print f1
'''
        



