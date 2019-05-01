mat=[
[ '*','*','*','*','*','*'],
[ '*','*','*','*','*','*'],
[ '*','*','*','*','*','*'],
[ '*','*','*','*','*','*'],
[ '*','*','*','*','*','*'],
[ '*','*','*','*','*','*']
]

def check_matrix3X3():
    cnt=0
    for i  in range(6):
        for j in range(6):
            if validate(i,j,3):
                cnt+=1
    return cnt

def check_matrix2X2():
    cnt=0
    for i  in range(6):
        for j in range(6):
            if validate(i,j,2):
                cnt+=1
    return cnt
def place_matrix2(user):
    flag=0
    for i in range(6):
        for j in range(6):
            if validate(i,j,user):
                place_matrix(i,j,user)
                flag=1
                break
        if flag==1:
            break

def print_matrix():
    for i in range(6):
        for j in range(6):
            print(mat[i][j],end=" ")
        print()

def place_matrix(x,y,z):
    for i in range(x,x+z):
        for j in range(y,y+z):
            mat[i][j]="1"

def validate(x,y,z):
    if (x+z-1)>5 or (y+z-1)>5:
        return False
    for i in range(x,x+z):
        for j in range(y,y+z):
            if mat[i][j]=="1":
                return False
    return True
def computer_check(user,level):
    if level==1 and user==3:
        place_matrix2(3)
    elif level==1 and user==2:
        place_matrix2(3)
    elif level==2:
        place_matrix2(user)
    elif level==3:
        place_matrix2(2)
def assign_mat(mm):
    prev = [
        ['*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*']
    ]
    for i in range(6):
        for j in range(6):
            prev[i][j]=mm[i][j]
    return prev


level=1

while(1):
    prev_matrix=assign_mat(mat)
    flag = 0
    user=int(input("Enter your squared matrix(2*2 or 3*3): "))
    for i in range(6):
        for j in range(6):
            if validate(i,j,user):
                place_matrix(i,j,user)
                flag=1
                break
        if flag==1:
            break
    print()
    print()
    if prev_matrix==mat:
        print("Computer Win!!!!!")
        break
    print("user: ")
    print_matrix()
    print("Computer: ")
    computer_check(user,level)
    print_matrix()
    level+=1



