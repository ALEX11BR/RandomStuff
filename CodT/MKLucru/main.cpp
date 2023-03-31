#include <iostream>

using namespace std;

int a[100][100];
int ii[] = {1, 0, -1, 0}, ij[] = {0, -1, 0, 1};

bool okfill(int x, int y, int n, int m, int t)
{
	return x>0 && y>0 && x<=n && y<=m && a[x][y]==t;
}

void fill(int x, int y, int n, int m, int z)
{
	int t=a[x][y];
	a[x][y] = z;
	for (int k=0; k<4; k++)
	{
		if (okfill(x+ii[k], y+ij[k], n, m, t))
			fill(x+ii[k], y+ij[k], n, m, z);
	}
}

int main()
{
	int n,m,x,y;
	cin>>n>>m;
	for (int i=1; i<=n; i++)
		for (int j=1; j<=m; j++)
			cin>>a[i][j];
	cin>>x>>y; // coloana, linie
	fill(x, y, n, m, 9);
	for (int i=1; i<=n; i++)
	{
		for (int j=1; j<=m; j++)
		{
			cout<<a[i][j]<<" ";
		}
		cout<<'\n';
	}		
}
