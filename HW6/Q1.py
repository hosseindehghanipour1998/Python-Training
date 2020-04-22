def f(y,x):
    avg=(x+y)/2
    if x==y:
        print "fuck yeah",avg
    else:
        print avg,"?:\"
        guess = input()
        if guess ==1:
            f(avg+1,x)
        if guess == -1:
            f(y,avg-1)
        if guess == 0:
                print "fuck yeah",avg


'''
f(0,100)
                
'''
