#question No.2

def iIndexOf(str1):
    str1 = str1 + " "
    len1 = len(str1)
    
    i = 0
    while i <len1:
        if i==len(str1) or str1[i]==" " :
            return i-1
        i+=1



