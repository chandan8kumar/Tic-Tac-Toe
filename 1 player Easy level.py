from Function import *
import random
print 'Welcome to TIC-TAC-TOE'
a=['1','2','3']
b=['4','5','6']
c=['7','8','9']
input_list=[1,2,3,4,5,6,7,8,9]
print a,'\n',b,'\n',c
flag1=0
#choice for characters for the player
m='X'
n='O'
m=input("Player enter your character: ")
if m=='X':
    n='O'
    flag1=1
elif m=='O':
    n='X'
    flag1=1
#Error handling
elif(m!='X' and n!='O')or(m!='O' and n!='X'):
    while flag1==0:
        m=input("Player enter VALID character: ")
        if m=='X':
            n='O'
            flag1=1
            break
        elif m=='O':
            n='X'
            flag1=1
            break
        else:
            flag1=0
#Game starts       
for i in range(9):
    x=input("Enter location for %c: "%m)
    flag2=0;
    if x in input_list:
        flag2=1
        mark(x,m,a,b,c)
        input_list.remove(x)
        if input_list==[]:
            break
    #Error handling
    else:
        while flag2==0:
            temp=input("Enter a VALID location for %c: "%m)
            if temp in input_list:
                flag2=1
                x=temp
                break
            else:
                flag2=0
        mark(x,m,a,b,c)
        input_list.remove(x)
        if input_list==[]:
            break
    if check(a,b,c)==1:
        print a,'\n',b,'\n',c
        print '%c WINS'%m
        break
    y=random.choice(input_list)
    if y in input_list:
        mark(y,n,a,b,c)
        input_list.remove(y)
        if input_list==[]:
            break
    if check(a,b,c)==1:
        print a,'\n',b,'\n',c
        print '%c WINS'%n
        break
    print a,'\n',b,'\n',c
if input_list==[] and check(a,b,c)==0:
    print 'TIE'
elif input_list==[] and check(a,b,c)==1:
    print a,'\n',b,'\n',c
    print '%c WINS'%m
