

mat=[
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*']
]


def mat_cr():
    print("[")
    for i  in range(10):
        print("[",end="")
        for j in range(10):
            print("'*'",end=",")
        print("],")
    print("],")


def check_matrix3X3():
    cnt=0
    for i  in range(10):
        for j in range(10):
            if validate(i,j,3):
                cnt+=1
    return cnt

def check_matrix2X2():
    cnt=0
    for i  in range(10):
        for j in range(10):
            if validate(i,j,2):
                cnt+=1
    return cnt
def place_matrix2(user):
    flag=0
    for i in range(10):
        for j in range(10):
            if validate(i,j,user):
                place_matrix(i,j,user)
                flag=1
                break
        if flag==1:
            break

def print_matrix():
    for i in range(10):
        for j in range(10):
            print(mat[i][j],end=" ")
        print()

def place_matrix(x,y,z):
    for i in range(x,x+z):
        for j in range(y,y+z):
            mat[i][j]="1"

def validate(x,y,z):
    if (x+z-1)>9 or (y+z-1)>9:
        return False
    for i in range(x,x+z):
        for j in range(y,y+z):
            if mat[i][j]=="1":
                return False
    return True
def computer_check():
    cnt3X3=check_matrix3X3()
    cnt2X2 = check_matrix2X2()
    if cnt3X3==1 :
        place_matrix2(3)
    elif cnt2X2 ==1 :
        place_matrix2(2)
    elif cnt3X3 % 2==1:
        place_matrix2(2)
    elif cnt2X2 % 2==1:
        place_matrix2(3)
    else:
        place_matrix2(3)

def assign_mat(mm):
    prev = [['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*','*','*','*']
]
    for i in range(10):
        for j in range(10):
            prev[i][j]=mm[i][j]
    return prev


level=1
while(1):
    prev_matrix=assign_mat(mat)
    flag = 0
    user=int(input("Enter your squared matrix(2*2 or 3*3): "))
    for i in range(10):
        for j in range(10):
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
    prev_matrix = assign_mat(mat)
    print("user: ")
    print_matrix()
    print("Computer: ")
    computer_check()
    print_matrix()
    level+=1
    if prev_matrix==mat:
        print("User Win!!!!!")
        break




