import Contains 
import Q2
def function(x,y):
    starter = 0
    starter1 = 0
    i = 0
    sentence = ""
    while starter<len(x):
        q2 = Q1.Q1(x[starter:],y)
        
        if q2 == -1:
            sentence = sentence + x[starter:]
            break
        
        else:     
            sentence = sentence + x[starter+1:q2+starter]
            starter = starter +q2 + len(y)
            
            
    return sentence
print function('word1 word2 word3 word4 word5 word6 word7 word8 word9 word10 word11','word12')
