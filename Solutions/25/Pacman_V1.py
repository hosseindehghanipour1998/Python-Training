def game_body():
    global score,tool,arz,foolist,cowall,path,score,cordall,go,alloldcord,allnewcord,cord,flag,joon,joonz,scores,sleeptime
    while flag == 1:
        cowall=BRICK_PRINTER(lines)    #brick print         
        foolist = FOOD_PRINTER(maxx,maxy,cowall) #food print
        score = 0
        path = ""
        cord=[1,1]
        tool=1
        arz=1
        cordall=[]
        alloldcordg =enemy_cord_maker(enemyNO) #makes old cord for enemy
        for item in alloldcordg:
            print Fore.RED+ "\033[" + str(int(item[1]))+";"+str(int(item[0]))+"H" +"E"
        go = ""
        while True:
            sleep(sleeptime)
            if kbhit():
                path = getch()
            alloldcordg=Enemies_move_print(alloldcordg,cowall,foolist)
            if (cord in alloldcordg):  #game over
                joon+=1
                print "\033[" + str(maxy+6) +";" + str(maxy+7)+"H"+"warning : joon = ",joon,"/",joonz
                if joon>= joonz:
                    Game_over()
                    break
            print Fore.WHITE + "\033["+str(cord[1])+";"+str(cord[0])+"H"+" " 
            cord=function_movement(path)
            print Fore.WHITE + "\033["+str(cord[1])+";"+str(cord[0])+"H"+"O"
            SCORE_CHECKER(foolist,cord)  #scores
            scores =SCORE_CHECKER(foolist,cord) #scores
            if (cord in alloldcordg):  #game over
                joon+=1
                print "\033[" + str(maxy+6) +";" + str(maxy+7)+"H"+"warning : joon = ",joon,"/",joonz
                if joon>= joonz:
                    Game_over()
                    break
            if len(foolist)==0: #game win
                you_win()
                break
#-----------------------------------------------------------------------------------
def Flag_maker_part():
    global command,flag,command2,hms
    while flag == 0:
        sleep(.12)
        system("cls")
        print " Hello, Welcome to Pacman "
        print "\n"
        print "1-Play Pacman"
        print "2-High Scores"
        print "3-options"
        print "4-Exit"
        command = input()
        flag = 0
        if command == 1:
            flag =1
            break
        if command == 2:
            flag = 2
            break
        if command !=1 or command !=2 or command!=3:
            flag = 0
        if command ==3:
            flag = 3
            break
        if command == 4:
            flag = -1
            break
#-------------------------------------------------------------------------------
def flag_executer_part():
    global flag,command2,joonz,hms,sleeptime,scoreslist
    while flag == 3:
        system("cls")
        print "1-joon max"
        print "2-highscore max"
        print "3-Speed" 
        command2 = input()
        if command2 == 1:
            system("cls")
            joonz = input("how many joonz?:")
            flag=0
            break
        if command2 ==2:
            system("cls")
            hms = input("how many hms:?")
            flag=0
            break
        if command2==3:
            system("cls")
            sleeptime = input("how fast you want it to be?:")
            flag = 0
            break
    while flag==2:
        print scoreslist
        sleep(4)
        flag = 0
        break
#---------------------------------------------------------------------------------
def map_reader():
    global lines,lenlines,len0,enemyNO,maxx,maxy
    mapfile = open("map.txt","r")  #reads the file
    lines = mapfile.readlines()        #puts them in a list  
    lenlines=len(lines)                   #the lenth of the list
    len0 = len(lines[0])                 #lenth of the page cordinates list
    enemyNO=int(lines[lenlines-1])   #number of the enemies
    #coordinates for app
    for i in range(len(lines[0])-1):
        if lines[0][i] ==" ":
            maxx=int(lines[0][:i])
            maxy=int(lines[0][i+1:len0-1])
#-------------------------------------------------------------------------------------

def Enemies_move_print(alloldcordg,cowall,foolist):
    for item in alloldcordg:
        if item in cowall :
            print Fore.CYAN+ "\033[" + str(int(item[1]))+";"+str(int(item[0]))+"H" +"D"
        if item in foolist:
            print Fore.GREEN+ "\033[" + str(int(item[1]))+";"+str(int(item[0]))+"H" +"#"
        if item not in cowall and item not in foolist:
            print Fore.BLACK+ "\033[" + str(int(item[1]))+";"+str(int(item[0]))+"H" +"G"
    allnewcordg=RANDOM_MOVE_CORD(alloldcordg)
    for item in allnewcordg:
        print Fore.RED+"\033[" + str(int(item[1]))+";"+str(int(item[0]))+"H" +"E"
    alloldcordg=allnewcordg
    return alloldcordg
#-------------------------------------------------GAME OVER-----------------------
def Game_over():
    global scoreslist,flag,joon
    scoreslist=Scores_adder(scores)
    scores_writer(scoreslist)
    system('cls')
    print "OOPS YOU LOST"
    sleep(3)
    flag=0
    joon=0
    
#-----------------------------YOU WIN----------------------------------------------
def you_win():
        system("cls")
        scoreslist=Scores_adder(scores)
        scores_writer(scoreslist)
        print "you won"
        sleep(4)
        flag=0
#---------------FUNCTIONS ARE DEFINED HERE-----------------------------------------
def function_movement(path):
    global tool
    global arz
    global cordall
    global go
    if path == 'w' or  path == 's' or path ==  'a' or path =='d' or  path=="p" :
        go = path
    if go == "w" and [tool,arz-1] not in cowall and arz>1 :
        arz -=1
    if go == "s"and [tool,arz+1] not in cowall and arz<maxy-1:
        arz+=1
    if go =="d"and [tool+1,arz] not in cowall and tool<maxx-1:
        tool+=1
    if go == "a" and [tool-1,arz] not in cowall and tool>1 : 
        tool-=1
    if go=="p":
        while True:
            c=getch()
            if c == "p":
                break
    cord=[tool,arz]
    cordall.append(cord)
    return cord
#-------------------------------------------FOOD PRINTER------------------------------------
def FOOD_PRINTER(maxx,maxy,cowall):
    foolist=[]
    for i in range(1,(maxx)): 
        for j in range(1,(maxy)):
             if [i,j] not  in cowall:       
                print Fore.GREEN+ "\033["+str(j)+";"+str(i)+"H#",
                print
                cofood=[]
                cofood.append(int(i))
                cofood.append(int(j))
                foolist.append(cofood)
    return foolist
#--------------------------------BRICK PRINTER-----------------------------------------------
def BRICK_PRINTER(lines):
    colist=[]
    cowall=[]
    bricksNO =int( lines[1])
    bc = lines[2:bricksNO+1]
    system("cls")
    for i in range(bricksNO-1):
        cordinates = bc[i]
        for i in range(len(cordinates)-1):
            if cordinates[i]==" ":
                colist  = []
                bx = cordinates[0:i]
                by=cordinates[i+1:len(cordinates)-1]
                colist.append(int(bx))
                colist.append(int(by))
                cowall.append(colist)
                print Fore.CYAN +"\033["+str(by)+";"+str(bx) +"H"+"D"
    return cowall
#------------------------------------------------SCORE---------------------------------------
def SCORE_CHECKER(foolist,cord):
    global maxx
    global maxy
    global score
    
    if cord in foolist:
        score+=1
        foolist.remove([cord[0],cord[1]])
        print  Fore.CYAN + "\033[" + str(maxy + 5) + ";" + str(maxx+5) +"H" + "score:",score
    return score

#----------------------------------ENEMY CORD MAKER---------------------------------------
def enemy_cord_maker(enemyNO):
    global maxx
    global maxy
    alloldcordg=[]
    for i in range(enemyNO):
        oldcordg = []
        xg = randint(maxx/2,maxx-1)
        yg=randint(maxy/2,maxy-1)
        oldcordg =[xg,yg]
        if oldcordg in alloldcordg:
            continue
        elif oldcordg not in alloldcordg:
            alloldcordg.append(oldcordg)
    return alloldcordg
#----------------------------------RANDOM MOVE CORD MAKER-----------------------------
def RANDOM_MOVE_CORD(allcordg):
    global cowall
    allnewcordg=[]
    for item in allcordg:
        randomNO=randint(1,4)
        newcord=[]
        tool=item[0]
        arz=item[1]
        if randomNO==1 and [tool,arz-1] not in cowall and arz>1 :
            arz -=1
        if randomNO==2 and [tool,arz+1] not in cowall and arz<maxy-1:
            arz+=1
        if  randomNO==3 and [tool+1,arz] not in cowall and tool<maxx-1:
            tool+=1
        if randomNO==4 and [tool-1,arz] not in cowall and tool>1 : 
            tool-=1
        newcord=[tool,arz]
        allnewcordg.append(newcord)
    return allnewcordg
#----------------------------------SCORES FILE MAKER------------------------------------------------
def score_file_maker():
    scoresfile=open("scores.txt","w+")
    scoresfile.write("0")
    scoresfile.close()
    return scoresfile
#----------------------------------SCORES LIST ORGANISER UPDATER---------------------------------------------
def Scores_adder(scores):
    scoresfile = open("scores.txt","r+")
    scoreslist1=scoresfile.readlines()
    scoresfile.close()
    scoreslist2 =scoreslist1[0].split()
    scoreslist3 = []
    for item in scoreslist2 :
        scoreslist3.append(int(item))
    len3=len(scoreslist3)
    print scoreslist3
    if len(scoreslist3)==hms:
        if scores > min(scoreslist3):
            scoreslist3.append(scores)
            scoreslist3.remove(min(scoreslist3))
    elif len(scoreslist3)<hms:
        scoreslist3.append(scores)
    return scoreslist3

#----------------------------------SCORE list writer--------------------------------------------    
def scores_writer(scoreslist):
    myfile=open("scores.txt","r+")
    for item in scoreslist:
        myfile.write(str(item))
        myfile.write(" ")
    myfile.close()
    
        
#----------------------------------SCORES SORTER--------------------------------------------
'''
def sorted_scores():
    newlist=[]
    myfile=open("scores.txt","r")
    lines2=myfile.readlines()
    maximum = max(lines2)
    print maximum

'''
#----------------------------------GAME STARTS HERE-----------------------------------------
#GAME'S DEFAULT NEEDS :
flag = 0
import colorama
from colorama import *
from os import system
import random
from random import *
from msvcrt import *
import time
from time import *

init()
#---------------------------------------------------------------------------------------------------
map_reader()
#MAKE THE SCORE FILE
sleeptime =0.12
score_file_maker()
hms = 5       
joon = 0
joonz = 1
scoreslist = [0]
#MENU BODY:
while True:
    Flag_maker_part()
    flag_executer_part()
    if flag == -1:
        system("cls")
        print "have a nice day"
        sleep(3)
        break
    #GAME BODY:
    game_body()
system("cls")
print "see you"
sleep(3)

        
