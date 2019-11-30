#question1 from assignment 7
def finder(jomle,kalame):

    len2 = len(kalame)
    len1 = len(jomle)
    i = 0
    while i <len1:
        if jomle[i] == kalame[0]:
            if jomle[i:i+len2] == kalame:
                return i
        i+=1
    return -1
########




def function5(jomle,kalame):
    #basic information
    list1 = []
    lenk = len(kalame)
    lenj = len(jomle)
    i = 0
    index = 0
#character checker
    while i < lenj:
        index =finder(jomle,kalame)
        print index
        #if function finds something it goes to this if statement
        if index != -1:
            list1 = list1 + [jomle[0:index]]
            print list1
            i =index + 1
            jomle = jomle[i+len(kalame)-1:]

        #if function didnt find the alphabet asked it goes to this statement
        if index == -1:
            list1 = list1 + [jomle[0:]]
            break 

    return list1

'''
print function5('in$$ the$$ name$$of$$Allah the most$$compassionate and merciful oh gosh','$$')

'''
