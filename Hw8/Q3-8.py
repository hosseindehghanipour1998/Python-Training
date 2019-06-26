def function3(a,b):
    if len(a)>=len(b):
        big = a
        small = b
    else:
        big = b
        small = a
    i = 0
    while i <len(small)-1:
        element = small[i]
        '''
        for item in big:
            if element ==item:
            return true
        '''
        for i in range(0, len(big)-1):
            if element == big[i]:
                return True
        i+=1
    return False

#Example:
'''
a  = [1,2,3,4]
b = [2,3,4]
print function3(a,b)

'''
