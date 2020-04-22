#3
'''
def function3(list1):
    while True:
        input1 = input("chia nazarete?:")
        if input1 !=0:
           list1.append(input1)
        if input1 == 0:
            break
    return list1
list2=[1,2,3,4,5]
print function3(list2)
'''       
 '''       
#3-b
def function3_b():
    list1=[]
    while  True:
        input1 = input("chia nazarete?:")
        if input1 != 0:
            list1 = list1 + [input1]
        if input1 == 0:
            break
    return list1
print function3_b()
'''
