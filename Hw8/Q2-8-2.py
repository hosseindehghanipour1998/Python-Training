def function2(a):
    c = len(a)
    maze = 0
    len1 = len(a)
    i = 1
    while c>0:
        while i <len1: 
            if a[0]==a[i]:
                maze +=1
                del a[i]
                len1 = len(a)
                i-=1
            i+=1
        print a[0],":",maze+1
        del a[0]
        maze = 0        
        c = len(a)
        len1 =len(a)
        i =1

