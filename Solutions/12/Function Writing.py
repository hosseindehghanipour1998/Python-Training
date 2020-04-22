def f(input2):
    
    counter = 1
    sum1 = 0
    while counter <= input2:
        num1 =(counter)*((-1)**counter)
        sum1 = sum1 + num1
        counter+=1
    return abs(sum1)*input2
