def functionplus(symbol,number):
    list1 = []
    i = 0
    while i<number:
        list1 = list1 + [symbol]
        i+=1
    return list1



def function4(m,n,p):
    list3 = functionplus('*',p)
    list2 = functionplus(list3,n)
    list1 = functionplus(list2,m)
    return list1


#Example :print function4(2,3,2)






'''
#Another Way
def function4(a,b,c):
    list3 = ["*"]*c
    list2 = [list3]*b
    list1 = [list2]*a
    return list1
print function4(2,3,2)
    
'''
