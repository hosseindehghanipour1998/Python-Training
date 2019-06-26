#question No.1


#to make it easy , i defined a function named EMF(flag,jomle)





def EMF(flag,jomle):
    len1 = len(jomle)
    while flag <=len1:
        if  flag==len1 or jomle[flag]==" ":
            index = flag
            return index
        flag +=1











def Q1(jomle,kalame):


    #str1 = input("jomle?:")
    #str2 = input("kalame?:")
    len1 = len(jomle)
    len2 = len(kalame)

    flag = 0
    while flag < len1:
        index = EMF(flag,jomle)
        len_word1 = index - flag
        if len_word1==len2:
            if kalame == jomle[flag:index]:
                return flag
        flag = index+1
    return -1
'''
print Q1('dear my friend the greatest the best ali the son of hossein','hossein')
print Q1('dear my friend the greatest the best ali the son of hossein','greatest')
print Q1('dear my friend the greatest the best ali the son of hossein','dera')
print Q1('dear my friend the greatest the best ali the son of hossein','ali')
print Q1('dear my friend the greatest the best ali the son of hossein','dear')
print Q1('hello world','world')
print Q1('hello world','word')
print Q1('world','world')
'''





                
    











