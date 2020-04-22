def createFile(a,b):
    myfile = open(a,'w+')
    myfile.write(b)
    myfile.close()
#function('this name is a test.txt','hello my graders')

def appendToFile(a,b):
    myfile = open(a,'a+')
    myfile.write(b) 
    myfile.write("\n")
    myfile.close()
#Example : function2('function2.txt','hello my name is hossein'),function2('function2.txt','hello my second friend in the second line')

def readFromFile(a,b):
    myfile = open(a,'a+')
    list3 = myfile.readlines()
    for i in len(list3):
        print list3[i]
        print i+1
        i+=1
    myfile.close()
#Example3:

def deleteFromFile(a,b):
    myfile = open(a,'r+')
    list4= myfile.readlines()
    print list4
    del list4[b-1]
    print list4
    myfile.seek(0,0)
    myfile.writelines(list4)
    myfile.close()

#Example : function4('hi.txt',2)

    
