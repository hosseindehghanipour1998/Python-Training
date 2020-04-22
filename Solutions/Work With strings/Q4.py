#question No.4
def replace(n):#n = hello
    p = len(n)-1
    if p==0:
        return n[0]
    else:
        
        return n[p] + Q4(n[0:p])
'''
print Q4('hello my friends')

'''
