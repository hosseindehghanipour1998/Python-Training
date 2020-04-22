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

def NNR():
    i = 0
    while i<2:
        input1 = input("chi nazarete?:\t")
    
        
        function = nice(input1)
        if function ==True:
            
            return input1


print f(function(NNR()))
'''
nnr = NNR()
function1 = function(nnr)
f1 = f(function1)
print f1
'''
       