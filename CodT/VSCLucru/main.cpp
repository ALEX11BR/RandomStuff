#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

ifstream fin("taietura.in");
ofstream fout("taietura.out");

int e[100000],c[100000];
vector<long long> s,ss,r;

int main()
{
	int n,i,p,p0;
	long long rr=0;
	fin>>n>>e[0];
	s.push_back(e[0]);
	for (i=1;i<n;i++)
	{
		fin>>e[i];
		s.push_back(s[i-1]+e[i]);
	}
	s.push_back(0);
	ss=s;
	sort(s.begin(),s.end());
	s.erase(unique(s.begin(),s.end()),s.end());

	p0=lower_bound(s.begin(),s.end(),0)-s.begin();
	c[p0]++; r.push_back(0);
	for (i=0;i<n;i++)
	{
		p=lower_bound(s.begin(),s.end(),ss[i])-s.begin();
		c[p]++;
		r.push_back(1-c[p]);
	}

	c[p0]--; r[0]+=c[p0];
	for (i=0;i<n-1;i++)
	{
		p=lower_bound(s.begin(),s.end(),ss[i])-s.begin();
		c[p]--;
		r[i+1]+=c[p];
	}

	for (i=0;i<n;i++)
	{
		rr+=r[i];
		fout<<rr<<" ";
	}
	return 0;
}