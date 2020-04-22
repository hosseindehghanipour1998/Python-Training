import IndexOf as Q2

def Q3(x):
    index = Q2.Q2(x)
    sentence = ""
    sentence = x[0:index+1] + sentence
    while index <len(x):
        b = index
        index = Q2.Q2(x[index+2: ])+b + 2
        sentence =x[b+1:index+2] + sentence
    return sentence
    
'''
print Q3("dear my graders my frinds and goods")

'''
