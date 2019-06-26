a = input("1st date?:")
aa = input("1st month?:")
b = input("2nd date?:")
bb = input("2nd month?:")
if aa <=6 and aa >=1:
    c = 31 - a
else:
    c = 30 -a
if bb >=1 and bb <=6:
    d = 31 - b
else:
    d = 30 - b
if (aa and bb <=6) and (aa and bb >=1):
    jbmd = abs(bb - aa -1 )*31
if (aa and bb <=12) and (aa and bb >=6):
    jbmd = abs(bb -aa -1)*30
if (1<= aa <=6) and (7<= bb <=12):
    jbmd = (abs(6-aa)*31) +(abs(bb - 7)*30)
    d = abs(1 - b)
if (1<= bb <=6) and (6<= aa <=12):
    jbmd = (abs(6-bb)*31) +(abs(aa - 7)*30)
    c = abs(1 - a)
output = jbmd + c + d
print (output)
raw_input ("press <enter to leave>")
'''
1st date = a
1st month = aa
2nd date = b
2nd month =bb
dif 1st date = c
dif 2nd date = d

'''
