#--------------------------------------------------------
def fact(n):
    if n==0 or n==1:
        return n
    return fact(n-1)*n
#--------------------------------------------------------
def strrev(str1):
    strlen=len(str1)
    if strlen==1:
        return str1
    else:
        return str1[strlen-1] + strrev(str1[:strlen-1])
#--------------------------------------------------------
def power(x,n):
    if x==0 and n!=0:
        return False
    elif n==1:
        return True
    elif n%x!=0:
        return False
    else:
        return power(x,n/x)
#--------------------------------------------------------
def hdigit(x):
    if x<1:
        return 0
    else:
        return 1+hdigit(x//10)
#--------------------------------------------------------
def myMax(list):
    listlen=len(list)
    if listlen==1:
        return list[0]
    else:
        MaxOfOthers=myMax(list[1:])
        if list[0]>MaxOfOthers:
            return list[0]
        return MaxOfOthers
#--------------------------------------------------------
def find(list1,x):
    for i in range(len(list1)):
        if type(list[i])==list:
            boolean=find(list[i],x)
            if boolean:
                return True
        elif list1[i]==x:
            return True
    return False
#--------------------------------------------------------
def 
        
