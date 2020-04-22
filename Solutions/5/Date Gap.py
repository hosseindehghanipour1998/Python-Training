1st date = input("1st date?:")
1st month = input("1st month?:")
2nd date = input("2nd date?:")
2nd month = input("2nd month?:")
if 1st month <=6 and 1st month >=1:
    dif 1st date = 31 - 1st date
else:
    dif 1st date = 30 -1st date
if 2nd month >=1 and 2nd month <=6:
    dif 2nd date = 31 - 2nd date
else:
    dif 2nd date = 30 - 2nd date
if (1st month and 2nd month <=6) and (1st month and 2nd month >=1):
    jbmd = abs(2nd month - 1st month -1 )*31
if (1st month and 2nd month <=12) and (1st month and 2nd month >=6):
    jbmd = abs(2nd month -1st month -1)*30
if (1<= 1st month <=6) and (7<= 2nd month <=12):
    jbmd = (abs(6-1st month)*31) +(abs(2nd month - 7)*30)
    dif 2nd date = abs(1 - 2nd date)
if (1<= 2nd month <=6) and (6<= 1st month <=12):
    jbmd = (abs(6-2nd month)*31) +(abs(1st month - 7)*30)
    dif 1st date = abs(1 - 1st date)
out put = jbmd + dif 1st date + dif 2nd date
print (out put)
raw_input ("press <enter to leave>")
'''
1st date = a
1st month = aa
2nd date = b
2nd month =bb
dif 1st date = c
dif 2nd date = d

'''
