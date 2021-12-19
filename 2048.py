import random

def start():
    a=[]
    for i in range(4):
        a.append([0,0,0,0])
    return a
# print(start())
def Print(a):                                                 #To print Matrix
    for j in a:
        for i in j:
            if i==0:
                print("  ",0,end="  ")
            elif i%1024 == 0 or i%2048==0:
                print(i,end="  ")
            elif i%128==0 or i%256==0 or i%512==0:
                print(" ",end="")
                print(i,end="  ")
            elif i%16==0 or i%32==0 or i%64==0:
                print("  ",end="")
                print(i,end="  ")
            else:
                print("   ",end="")
                print(i,end="  ")


        print()
def new(mat):                                                      #To add new element
    count=0
    for i in mat:
        for j in i:
            if j!=0:
                count=count+1
        if count==16:
            return mat

    r=random.randint(0,3)
    c=random.randint(0,3)
    while mat[r][c]!=0:
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2


def status(mat):                                           #checking status of game
    for i in mat:
        for j in i:
            if j==2048:
                return 3
    for i in mat:
        for j in i:
            if j==0:
                return
    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i][j+1]:
                return
    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i+1][j]:
                return
    for j in range(3):
        if mat[3][j]==mat[3][j+1]:
            return
    for j in range(3):
        if mat[j][3]==mat[j+1][3]:
            return
    return 1
def move(mat):                                      #To move numbers to left and zeroes to right
    y=[]
    for i in range(4):
        y.append([0,0,0,0])


    for i in range(4):
        p=0
        for j in range(4):
            if mat[i][j]!=0:
                y[i][p]=mat[i][j]
                p=p+1
    return y
def add(mat):                                        #To add adjacent two numbers
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                mat[i][j]=mat[i][j]*2
                mat[i][j+1]=0
def mirror(mat):                                    #To create a mirror image
    y=start()
    for i in range(4):
        for j in range(4):
            y[i][j]=mat[i][3-j]
    return y
def trans(mat):                                     #Transpose of a matrix
    y=start()
    for i in range(4):
        for j in range(4):
            y[i][j]=mat[j][i]
    return y

def move_left(mat):
    c=move(mat)
    add(c)
    d=move(c)
    return d
def move_right(mat):
    c=mirror(mat)
    d=move(c)
    add(d)
    e=move(d)
    e=mirror(e)

    return e
def move_up(mat):
    c=trans(mat)
    d=move(c)
    add(d)
    d=move(d)
    d=trans(d)
    return d
def move_down(mat):
    c=trans(mat)
    d=mirror(c)
    d=move(d)
    add(d)
    d=move(d)
    d=mirror(d)
    d=trans(d)
    return d
mat=start()
new(mat)
Print(mat)
s=True
while s:                                    # User input
    i = input()
    if i=="U":
        mat=move_up(mat)
    elif i=="D":
        mat=move_down(mat)
    elif i=="R":
        mat=move_right(mat)
    elif i=="L":
        mat=move_left(mat)
    else:
        print("Invalid Key Entered")
    r=status(mat)
    new(mat)
    Print(mat)
    if r==1:
        s=False
        print("GAME OVER")
    elif r==3:
        s=False
        print("YOU WON")
