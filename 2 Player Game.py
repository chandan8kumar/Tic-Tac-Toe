from Function import *
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
m=input("Player 1 enter your character: ")
n=input("Player 2 enter your character: ")
if(m=='X' and n=='O')or(m=='O' and n=='X'):
    flag1=1
#Error handling
else:
    while flag1==0:
        m=input("Player 1 enter VALID character: ")
        n=input("Player 2 enter VALID character: ")
        if(m=='X' and n=='O')or(m=='O' and n=='X'):
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
        print a,'\n',b,'\n',c
        if input_list==[]:
            if check(a,b,c)==1:
                print '%c WINS'%m
                break
            else:
                break
    #Error handling
    else:
        while flag2==0:
            x=input("Enter a VALID location for %c: "%m)
            if x in input_list:
                flag2=1
                break
            else:
                flag2=0
        mark(x,m,a,b,c)
        input_list.remove(x)
        print a,'\n',b,'\n',c
        if input_list==[]:
            if check(a,b,c)==1:
                print '%c WINS'%m
                break
            else:
                break
    if check(a,b,c)==1:
        print '%c WINS'%m
        break
    y=input("Enter location for %c: "%n)
    flag3=0
    if y in input_list:
        flag3=1
        mark(y,n,a,b,c)
        input_list.remove(y)
        print a,'\n',b,'\n',c
        if input_list==[]:
            if check(a,b,c)==1:
                print '%c WINS'%n
                break
            else:
                break
    else:
        while flag3==0:
            y=input("Enter a VALID location for %c: "%n)
            if y in input_list:
                flag3=1
                break
            else:
                flag3=0
        mark(y,n,a,b,c)
        input_list.remove(y)
        print a,'\n',b,'\n',c
        if input_list==[]:
            if check(a,b,c)==1:
                print '%c WINS'%n
                break
            else:
                break
    if check(a,b,c)==1:
        print '%c WINS'%n
        break
if input_list==[] and check(a,b,c)==0:
    print 'TIE'
