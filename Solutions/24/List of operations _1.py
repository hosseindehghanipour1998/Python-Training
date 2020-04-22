




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








def factor_finder1(x):
    result = 1
    i = 2
    while i<x:
        mod = x%i
        if mod == 0:
            c = prime_check(i)
            if c ==True:
                result = result * i
        i+=1
    return result







    
def factor_finder2(x):
    result = 1
    i = 2
    max2 = 2
    while i<=x:
        mod = x%i
        if mod == 0:
            c = prime_check(i)
            if c ==True:
                if i>=max2:
                    max2=i
        i+=1
    return max2








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
            print factor_finder1(number)


        if answer ==2:
            print factor_finder2(number)


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
            
                        




