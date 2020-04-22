def function2(a):
    c = len(a)
    maze = 0
    len1 = len(a)
    i = 1
    while c>0:
        while i <len1: 
            if a[0]==a[i]:
                maze +=1
                '''
                instead of next 4 lines:
                del a[i]
                 '''
                if i!=0:
                    a = a[0:i] + a[i+1:]
                elif i == 0:
                    a = a[1:]
                        
                len1 = len(a)
                i-=1
            i+=1
        print   a[0],":",maze+1
        a =a[1:]    #del a[0]    instead of a = a[1:]
        maze = 0        
        c = len(a)
        len1 =len(a)
        i =1



#Example:
'''
b = [1,2,'python',2,3,'hello','python','reza','reza','python','python',2,2,2,2,2,4,5,3,4,5,4,2,3,5,67,8,6,4,3,56,73,2]
function2(b)
'''

