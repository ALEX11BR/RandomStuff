#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

ifstream fin("taietura.in");
ofstream fout("taietura.out");

int main()
{
	int a,b;
	fin>>a>>b;
	fout<<a+b;
	return 0;
}
