#question No.6
#in the name of God

def Q6(string2,index,string1):
    sentence = ""
    i = 0
    while i <index:
        sentence = sentence + string1[i]
        i+=1
    sentence = sentence + string2
    b = index
    while b <len(string1):
        sentence = sentence + string1[b]
        b+=1
    return sentence
        
#example 1:print Q6('hello',3,'word1 word2')
#example 2:print Q6('compassionate',30,'in the name of allah the most and merciful')
#example 3:print Q6('friend',8,'hello my')
'''
tooye in soal ghaedatan bayad ye space bede beine "my & friend"(example 3) vali
choon khodetoon toye example haii ke gozashtid in mozoo ro dar nazar nagerefte boodid man ham dar nazar nagereftamesh.
'''
