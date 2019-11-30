n = input('what is the string?:\n')
def length(n):
    count = 0
    for char in n:
        count+=1
    return count
print length(n)
