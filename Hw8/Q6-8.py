def function(a):
    b = []
    for i in range (len(a)):
        if type(a[i])  != list:
            b = b+[a[i]]
        if type(a[i])==list:
            c = function(a[i])
            b = b+[c]
    return b


'''
x=[[1, 2, 3], 2, 3, 4, 5, 6, 7, 8, 9]
y =function(x)
'''

#another way
'''
import copy
copy.deepcopy
'''
