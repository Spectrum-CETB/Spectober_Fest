#include <bits/stdc++.h>
using namespace std;
int solution(string s)
{
	long long int n = 0;
	int si = s.size();
	for (int i = 0; i < si; i++)
	{
		if (s[i] == 'I')
		{
			if ((s[i + 1] == 'V' || s[i + 1] == 'X') && i != si - 1)
				n--;
			else
				n++;
		}
		if (s[i] == 'X')
		{
			if (s[i + 1] == 'L' || s[i + 1] == 'C')
				n -= 10;
			else
				n += 10;
		}
		if (s[i] == 'C')
		{
			if (s[i + 1] == 'D' || s[i + 1] == 'M')
				n -= 100;
			else
				n += 100;
		}
		if (s[i] == 'M')
			n += 1000;
		if (s[i] == 'D')
			n += 500;
		if (s[i] == 'L')
			n += 50;
		if (s[i] == 'V')
			n += 5;
	}
	return n;
}
int main()
{
	string test;
	cin >> test;
	cout<<solution(test)<<endl;
	return 0;
}