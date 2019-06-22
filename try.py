mat=[
[ '*','*','*','*','*','*'],
[ '*','*','*','*','*','*'],
[ '*','*','*','*','*','*'],
[ '*','*','*','*','*','*'],
[ '*','*','*','*','*','*'],
[ '*','*','*','*','*','*']
]
def validate(x,y,z):
    if (x+z-1)>5 or (y+z-1)>5:
        return False
    for i in range(x,x+z):
        for j in range(y,y+z):
            if mat[i][j]=="1" or mat[i][j]=="0":
                return False
    return True
def print_matrix():
    for i in range(6):
        for j in range(6):
            print(mat[i][j],end=" ")
        print()
    print()
def place_matrix(x,y,z):
    for i in range(x,x+z):
        for j in range(y,y+z):
            mat[i][j]="1"

def place_matrix3(x,y,z):
    for i in range(x,x+z):
        for j in range(y,y+z):
            mat[i][j]="0"

def place_matrix2(user):
    flag=0
    ch=0
    for i in range(6):
        for j in range(6):
            if validate(i,j,user):
                place_matrix3(i,j,user)
                flag=1
                ch=1
                break
        if flag==1:
            break
    return ch


def computer_check(user,level):

    if level==1 and user==3:
        v=place_matrix2(3)
    elif level==1 and user==2:
        v=place_matrix2(3)
    elif level==2 and user == 2 and first==2:
        v=place_matrix2(2)
    elif level==2 and user == 2:
        v=place_matrix2(3)
    elif level==2 and user == 3:
        v=place_matrix2(3)

    elif level==3:
        v=place_matrix2(2)
    else:
        v=place_matrix2(2)
    return v
label=1
print("User=1 and AI=0")
global first
while(1):
    flag=0
    check=0
    user = int(input("Enter your squared matrix(2*2 or 3*3): "))

    if label==1:
        first=user
    for i in range(6):
        for j in range(6):
            if validate(i,j,user):
                place_matrix(i, j, user)
                print("User:")
                print_matrix()
                check=1
                flag=1
                break
        if flag == 1:
            break

    if check == 0:
        print("AI win !!!!")
        break

    print("AI:")
    v=computer_check(user, label)
    label = label + 1
    if v==0:
        print("user win !!!!")
        break
    print_matrix()
cnt=0
while(1):
    if cnt==0:
        cnt=1
        print("Game over !!!!!")
    pass