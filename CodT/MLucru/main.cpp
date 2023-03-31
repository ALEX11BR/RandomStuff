#include <iostream>

using namespace std;

int a[100][100];

int main()
{
    int n,i,j,k; bool ok;
    cin>>n;
    for (i=1;i<=n;i++)
    {
        for (j=1;j<=n;j++)
        {
            cin>>a[i][j];
        }
    }
    do
    {
        ok=0;
        for (i=1;i<n;i++)
        {
            if (a[i][i]>a[i+1][i+1])
            {
                ok=1;
                for (j=1;j<=n;j++)
                {
                    k=a[i][j];
                    a[i][j]=a[i+1][j];
                    a[i+1][j]=k;
                }
                for (j=1;j<=n;j++)
                {
                    k=a[j][i];
                    a[j][i]=a[j][i+1];
                    a[j][i+1]=k;
                }
            }
        }
    }
    while (ok);
    for (i=1;i<=n;i++)
    {
        for (j=1;j<=n;j++)
        {
            cout<<a[i][j]<<'\t';
        }
        cout<<'\n';
    }
    return 0;
}
