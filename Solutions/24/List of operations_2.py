def factor_finder(x):
    list121 = []
    global list121
    i = 2
    while i<x:
        mod = x%i
        if mod == 0:
            list121.append(i)
        i+=1





def prime_check(x):
    i = 2
    if x!=2:
        while i<x:
            mod = x% i
            if mod == 0:
                return False
            if mod!=0:
                i+=1
        if mod !=0:
            return True
    elif x ==2:
        return True




def prime_factors(x):
    primelist = []
    global primelist
    factor_finder(x)
    result = 1
    for u in list121:
        prime_check(u)
        if prime_check(u) == True:
            primelist.append(u)


        #START#

def function():
    
    number = input('what is the number?:\n')
    print '''
                1- multiple of factors
                2-greatest prime divisor
                3-calculates poly
                4-calculates a.n
                5-change base
                6-change number
                7-exit
                    '''

    while True:
       
        answer = input("what is your choice?:\n")


        if answer ==1:
            prime_factors(number)
            result1 = 1
            for u in primelist:
                result1 = result1 * u
            print result1


        if answer ==2:
            print max(primelist)


        if answer == 3:
            n = input('ba che tavani start bezanam?:\n')
            sum1 = 0
            while n>=0:
                zarib = input('che zaribi:')
                result = zarib * (number**n)
                sum1 = sum1 +result
                n-=1
            print sum1

        if answer == 4:
            import math
            degree = input('what is the degree?:\n')
            n = input("what is the first vector?:\n")
            teta = math.radians(degree)
            cos2 = math.cos(teta)
            result1 = n * number *cos2
            print result1



        if answer == 5:
            base = input("what base is that?:\n")
            i = 0
            sum1 = 0
            while number>0:
                mod = number%base
                number = number/base
                i+=1
                sum1 = sum1 + mod*10**(i-1)
            print sum1



        if answer == 6:
            function()

        if answer == 7:
            print 'have a nice day and goodbye'
            break
    
function()
            
                        




