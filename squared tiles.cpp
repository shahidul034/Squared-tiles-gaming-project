#include<bits/stdc++.h>
using namespace std;
string mat[6][6];
int first;

int place_matrix3(int x,int y,int z)
{
    for (int i=x; i<(x+z); i++)
    {
        for (int j=y; j<(y+z); j++)
        {
            mat[i][j]="0";

        }

    }


}
bool validate(int x,int y,int z)
{
    if ((x+z-1)>5 || (y+z-1)>5)
    {
        return false;


    }

    for (int i=x; i<(x+z); i++)
    {
        for(int j=y; j<(y+z); j++)
        {
            if (mat[i][j]=="1" || mat[i][j]=="0")
                return false;

        }

    }

    return true;

}
int print_matrix()
{
    for (int i=0; i<6; i++)
    {
        for (int j=0; j<6; j++)
        {
            cout<<mat[i][j]<<" ";

        }
        cout<<endl;

    }


}


int place_matrix2(int user)
{
    int flag=0;
    int ch=0;
    for (int i=0; i<6; i++)
    {
        for (int j=0; j<6; j++)
        {
            if (validate(i,j,user))
            {
                place_matrix3(i,j,user);
                flag=1;
                ch=1;
                break;
            }

        }
        if (flag==1)
            break;


    }
    return ch;



}


int place_matrix(int x,int y,int z)
{
    for (int i=x; i<(x+z); i++)
    {
        for (int j=y; j<(y+z); j++)
        {
            mat[i][j]="1";

        }

    }
}




int computer_check(int user,int level)
{
    int v;

    if (level==1 && user==3)
    {
        v=place_matrix2(3);
    }

    else if (level==1 && user==2)
    {
        v=place_matrix2(3);
    }

    else if (level==2 && user == 2 and first==2)
    {
        v=place_matrix2(2);
    }

    else if (level==2 && user == 2)
    {
        v=place_matrix2(3);
    }

    else if (level==2 && user == 3)
    {
        v=place_matrix2(3);

    }

    else if (level==3)
    {
        v=place_matrix2(2);
    }

    else
    {
        v=place_matrix2(2);
    }

    return v;



}





int main()
{
    int label=1;

    for(int i=0; i<6; i++)
    {
        for(int j=0; j<6; j++)
        {
            mat[i][j]="*";
        }
    }
    while(1)
    {
        int flag=0;
        int check=0;
        int user;

        while(1)
        {
            printf("user input(2*2 and 3*3): ");
            cin>>user;
            if(user==2 || user==3)
            {
                break;
            }
        }


        if (label==1)
        {
            first=user;
        }

        for (int i=0; i<6; i++)
        {
            for (int j=0; j<6; j++)
            {
                if (validate(i,j,user))
                {
                    place_matrix(i, j, user);
                    printf("User:\n");
                    print_matrix();
                    check=1;
                    flag=1;
                    break;
                }

            }
            if (flag==1)
            {
                break;
            }

        }
        if (check == 0)
        {
            printf("AI win !!!!\n");
            break ;
        }
        printf("AI:\n");
        int v=computer_check(user, label);
        label = label + 1;
        if (v==0)
        {
            printf("user win !!!!");
            break;
        }
        print_matrix();


    }

}
