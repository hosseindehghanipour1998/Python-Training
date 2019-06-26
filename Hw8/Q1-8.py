def FLC(a):
    len1 = len(a)
    if a[0]==a[len1-1]:
        return True

def function1(list1):
    counter =0
    for item in list1:
        if len(item)>=2:
            ans = FLC(item)
            if ans == True:
                counter +=1
    print counter





#example
'''
b = ['abc','xyz','aba','1221','aabbaa','11']
function1(b)
'''
