#problem set 8
'''
#-1
string = raw_input('what is the string?:')
len1=len(string)
for i in range( len1):
    print string[i],"\n"
'''
'''
#-3
def function3(string1,string2):
    if string1>string2:
        return "1"
    if string2>string1:
        return -1
    if string1==string2:
        return 0
str1 = "hello my friend"
str2="how are you?"
print function3(str1,str2)
'''
'''
#4-
def function4():
    input1 = raw_input("what is the text?:")
    input2=raw_input("what is the character?:")
    for i in range( len(input1)):
        if input2 == input1[i]:
            return i
    return -1
print function4()
'''
'''
#-5
def function5():
    input1 = raw_input("string 1?:")
    input2 = raw_input("characters?:")
    for i in range(len(input1)):
        if input1[i] == input2[0]:
            if input1[i:len(input2)+i] == input2:
                return True
    return False
    
print function5()
'''
'''
def function6(string,char):
    print len(string)
    for i in range(len(string)):
        print "1st"
        if string[i]==char:
            if char in string[i+1:]:
                print True
                for j in range (len(string[i+1:])):
                    print "2nd"
                    if string[i+1+j] == char:
                        return string[i+1:j+i+1]
                    
            else:
                return string[i+1:]

string = "hello g my friend g"
char = "g"
print function6(string,char)
'''
'''
#7-
def function7():
    string = raw_input("string?:")
    len1 = len(string)
    list1=string.split()
    list1.reverse()
    return " ".join(list1)
   
print function7()
'''
    
    
