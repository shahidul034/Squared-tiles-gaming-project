mat=[
[ '*','*','*','*','*','*'],
[ '*','*','*','*','*','*'],
[ '*','*','*','*','*','*'],
[ '*','*','*','*','*','*'],
[ '*','*','*','*','*','*'],
[ '*','*','*','*','*','*']
]

def banner(text):


    username = text
    style = "#"
    space = ' '

    # two lists which store the value the input can take...
    style1 = ["*", "=", "@", "#", "$", "!", "~", "'", "^", "&", "|", "%", "-"]
    style2 = ["{}", "()", "[]", "<>"]

    # appends all the letters in style 1. I am really lazy to put them each in the list, so the computer will do that for me.
    for i in "abcdefghijklmnopqrstuvwxyz":
        style1.append(i)

    # finds all the indexes of a char in a string
    def find_indices(char, in_string):
        index = -1
        while True:
            index = in_string.find(char, index + 1)
            if index == -1:
                break
            yield index

    if style in style1:

        linie = style + style * len(username) + style + "\n"
        if " " in username:

            for i in find_indices(space, username):
                linie = list(linie)
                linie[i + 1] = " "
                linie = "".join(linie)

        print(linie + style + username + style + "\n" + linie)


    if style in style2:
        middle = "-"
        line = style[0] + len(username) * middle + style[1]
        if " " in username:
            for i in find_indices(space, username):
                line = list(line)
                line[i + 1] = " "
                line = "".join(line)
        print(line + "\n" + style[0] + username + style[1] + "\n" + line)


    if style.lower() == "bonus":
        line1 = "^" + "^" * len(username) + "^"
        line2 = "v" + "v" * len(username) + "v"
        if " " in username:
            for i in find_indices(space, username):
                line1 = list(line1)
                line2 = list(line2)
                line1[i + 1] = " "
                line2[i + 1] = " "
                line1 = "".join(line1)
                line2 = "".join(line2)
        print(line1 + "\n" + "<" + username + ">" + "\n" + line2)


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
def checkvalidation(user):
    return user==2 or user==3

def computer_check(user,level):

    if level==1 and user==3:
        v=place_matrix2(3)
    elif level==1 and user==2:
        v=place_matrix2(3)
    elif level==2 and user == 2 and first==2:
        v=place_matrix2(2)
    #elif level==2 and user == 2:
     #   v=place_matrix2(3)
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
    while(1):
        user = int(input("Enter your squared matrix(2*2 or 3*3): "))
        t=checkvalidation(user)
        if t==True:
            break



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
        banner("AI win !!!!")
        break

    print("AI:")
    v=computer_check(user, label)
    label = label + 1
    if v==0:
        banner("user win !!!!")
        break
    print_matrix()
cnt=0
while(1):
    if cnt==0:
        cnt=1
        banner("Game over !!!!!")
    pass