def check(a,b,c):
    '''Checks for the PATTERN in COLUMNS, ROWS and DIAGONALS and return 1 if found else return 0'''
    x=check_col(a,b,c)
    y=check_row(a,b,c)
    z=check_diag(a,b,c)
    return (x or y or z)
def check_col(a,b,c):
    '''Checks for the pattern in COLUMNS and return 1 if found else return 0'''
    for i in range(3):
        if a[i]==b[i]==c[i]:
            return 1
    return 0
def check_row(a,b,c):
    '''Checks for the PATTERN in ROWS and return 1 if found else return 0'''
    for i in range(1):
        if a[i]==a[i+1]==a[i+2]:
            return 1
        elif b[i]==b[i+1]==b[i+2]:
            return 1
        elif c[i]==c[i+1]==c[i+2]:
            return 1
    return 0
def check_diag(a,b,c):
    '''Checks for the PATTERN in DIAGONALS and return 1 if found else return 0'''
    for i in range(1):
        if a[i]==b[i+1]==c[i+2]:
            return 1
        elif c[i]==b[i+1]==a[i+2]:
            return 1
    return 0
def mark(location,letter,a,b,c):
    '''Marks the given LOCATION in MATRIX with LETTER'''
    if location<=3:
        a[location-1]=letter
    elif location<=6:
        b[location-4]=letter
    elif location<=9:
        c[location-7]=letter
#Intelligence for the Computer
def defend(letter,a,b,c,inputs,input_list):
    '''Defend the oponent by finding his/her next move'''
    p=defend_oponent(a,b,c,letter,inputs,input_list)
    if p==1:
        return 0
    return 1
def win_game(letter,a,b,c,inputs,input_list):
    '''win by finding his/her next move'''
    p=win(a,b,c,letter,inputs,input_list)
    if p==1:
        return 0
    return 1
def win(a,b,c,letter,inputs,input_list):
    '''Checks for the next move in ROWS if found then put a opposite sign on next move and return 1 else return 0'''
    for i in range(1):
        if a[i]==a[i+1]==letter:
            if a[i+2]!='X' or a[i+2]!='O':
                temp=inputs.get(a[i+2])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(a[i+2])
                    a[i+2]=letter
                    return 1
        elif a[i+1]==a[i+2]==letter:
            if a[i]!='X' or a[i]!='O':
                temp=inputs.get(a[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(a[i])
                    a[i]=letter
                    return 1
        elif a[i]==a[i+2]==letter:
            if a[i+1]!='X' or a[i+1]!='O':
                temp=inputs.get(a[i+1])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(a[i+1])
                    a[i+1]=letter
                    return 1
        elif b[i]==b[i+1]==letter:
            if b[i+2]!='X' or b[i+2]!='O':
                temp=inputs.get(b[i+2])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(b[i+2])
                    b[i+2]=letter
                    return 1
        elif b[i+1]==b[i+2]==letter:
            if b[i]!='X' or b[i]!='O':
                temp=inputs.get(b[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(b[i])
                    b[i]=letter
                    return 1
        elif b[i]==b[i+2]==letter:
            if b[i+1]!='X' or b[i+1]!='O':
                temp=inputs.get(b[i+1])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(b[i+1])
                    b[i+1]=letter
                    return 1
        elif c[i]==c[i+1]==letter:
            if c[i+2]!='X' or c[i+2]!='O':
                temp=inputs.get(c[i+2])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(c[i+2])
                    c[i+2]=letter
                    return 1
        elif c[i+1]==c[i+2]==letter:
            if c[i]!='X' or c[i]!='O':
                temp=inputs.get(c[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(c[i])
                    c[i]=letter
                    return 1
        elif c[i]==c[i+2]==letter:
            if c[i+1]!='X' or c[i+1]!='O':
                temp=inputs.get(c[i+1])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(c[i+1])
                    c[i+1]=letter
                    return 1
        elif a[i]==b[i+1]==letter:
            if c[i+2]!='X' or c[i+2]!='O':
                temp=inputs.get(c[i+2])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(c[i+2])
                    c[i+2]=letter
                    return 1
        elif b[i+1]==c[i+2]==letter:
            if a[i]!='X' or a[i]!='O':
                temp=inputs.get(a[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(a[i])
                    a[i]=letter
                    return 1
        elif a[i]==c[i+2]==letter:
            if b[i+1]!='X' or b[i+1]!='O':
                temp=inputs.get(b[i+1])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(b[i+1])
                    b[i+1]=letter
                    return 1
        elif c[i]==b[i+1]==letter:
            if a[i+2]!='X' or a[i+2]!='O':
                temp=inputs.get(a[i+2])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(a[i+2])
                    a[i+2]=letter
                    return 1
        elif b[i+1]==a[i+2]==letter:
            if c[i]!='X' or c[i]!='O':
                temp=inputs.get(c[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(c[i])
                    c[i]=letter
                    return 1
        elif c[i]==a[i+2]==letter:
            if b[i+1]!='X' or b[i+1]!='O':
                temp=inputs.get(b[i+1])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(b[i+1])
                    b[i+1]=letter
                    return 1
    for i in range(3):
        if a[i]==b[i]==letter:
            if c[i]!='X' or c[i]!='O':
                temp=inputs.get(c[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(c[i])
                    c[i]=letter
                    return 1
        elif b[i]==c[i]==letter:
            if a[i]!='X' or a[i]!='O':
                temp=inputs.get(a[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(a[i])
                    a[i]=letter
                    return 1
        elif a[i]==c[i]==letter:
            if b[i]!='X' or b[i]!='O':
                temp=inputs.get(b[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(b[i])
                    b[i]=letter
                    return 1
    return 0
def defend_oponent(a,b,c,letter,inputs,input_list):
    '''Checks for the next move in ROWS if found then put a opposite sign on next move and return 1 else return 0'''
    for i in range(1):
        if a[i]==a[i+1]:
            if a[i+2]!='X' or a[i+2]!='O':
                temp=inputs.get(a[i+2])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(a[i+2])
                    a[i+2]=letter
                    return 1
        elif a[i+1]==a[i+2]:
            if a[i]!='X' or a[i]!='O':
                temp=inputs.get(a[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(a[i])
                    a[i]=letter
                    return 1
        elif a[i]==a[i+2]:
            if a[i+1]!='X' or a[i+1]!='O':
                temp=inputs.get(a[i+1])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(a[i+1])
                    a[i+1]=letter
                    return 1
        elif b[i]==b[i+1]:
            if b[i+2]!='X' or b[i+2]!='O':
                temp=inputs.get(b[i+2])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(b[i+2])
                    b[i+2]=letter
                    return 1
        elif b[i+1]==b[i+2]:
            if b[i]!='X' or b[i]!='O':
                temp=inputs.get(b[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(b[i])
                    b[i]=letter
                    return 1
        elif b[i]==b[i+2]:
            if b[i+1]!='X' or b[i+1]!='O':
                temp=inputs.get(b[i+1])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(b[i+1])
                    b[i+1]=letter
                    return 1
        elif c[i]==c[i+1]:
            if c[i+2]!='X' or c[i+2]!='O':
                temp=inputs.get(c[i+2])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(c[i+2])
                    c[i+2]=letter
                    return 1
        elif c[i+1]==c[i+2]:
            if c[i]!='X' or c[i]!='O':
                temp=inputs.get(c[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(c[i])
                    c[i]=letter
                    return 1
        elif c[i]==c[i+2]:
            if c[i+1]!='X' or c[i+1]!='O':
                temp=inputs.get(c[i+1])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(c[i+1])
                    c[i+1]=letter
                    return 1
        elif a[i]==b[i+1]:
            if c[i+2]!='X' or c[i+2]!='O':
                temp=inputs.get(c[i+2])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(c[i+2])
                    c[i+2]=letter
                    return 1
        elif b[i+1]==c[i+2]:
            if a[i]!='X' or a[i]!='O':
                temp=inputs.get(a[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(a[i])
                    a[i]=letter
                    return 1
        elif a[i]==c[i+2]:
            if b[i+1]!='X' or b[i+1]!='O':
                temp=inputs.get(b[i+1])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(b[i+1])
                    b[i+1]=letter
                    return 1
        elif c[i]==b[i+1]:
            if a[i+2]!='X' or a[i+2]!='O':
                temp=inputs.get(a[i+2])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(a[i+2])
                    a[i+2]=letter
                    return 1
        elif b[i+1]==a[i+2]:
            if c[i]!='X' or c[i]!='O':
                temp=inputs.get(c[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(c[i])
                    c[i]=letter
                    return 1
        elif c[i]==a[i+2]:
            if b[i+1]!='X' or b[i+1]!='O':
                temp=inputs.get(b[i+1])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(b[i+1])
                    b[i+1]=letter
                    return 1
    for i in range(3):
        if a[i]==b[i]:
            if c[i]!='X' or c[i]!='O':
                temp=inputs.get(c[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(c[i])
                    c[i]=letter
                    return 1
        elif b[i]==c[i]:
            if a[i]!='X' or a[i]!='O':
                temp=inputs.get(a[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(a[i])
                    a[i]=letter
                    return 1
        elif a[i]==c[i]:
            if b[i]!='X' or b[i]!='O':
                temp=inputs.get(b[i])
                if temp in input_list:
                    input_list.remove(temp)
                    inputs.pop(b[i])
                    b[i]=letter
                    return 1
    return 0
