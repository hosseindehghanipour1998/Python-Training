#Q2-a
def a(x):
    i = 1
    while i<x:
        print i,
        i+=1
    while x>0:
        print x,
        x-=1
#-----------------------------------
        #Q2-b
def b(x):
    print x*"  ",
'''
or we can use this one:
def b(x):
    while i<x:
        print "  ",
        
'''
#-----------------------------------
    #Q2-c

def c(x):
    line = 1

    while line<=x:
        b(x - line)
        a(line)
        print
        line+=1
        
    line-=2
    while line>0:
        b(x-line)
        a(line)
        print
        line-=1
        
'''
c(8)
'''
