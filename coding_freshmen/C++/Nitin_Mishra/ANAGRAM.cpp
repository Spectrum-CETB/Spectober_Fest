#include <bits/stdc++.h>
using namespace std;
bool solution(string s,string t)
{
	if(s.size()!=t.size())
            return false;
        else
        {
            sort(s.begin(),s.end());
            sort(t.begin(),t.end());
            if(t==s)
                return true;
            else
                return false;
        }
}
int main()
{
	string test,str;
	cin >> test>>str;
    if(solution(test,str))
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;
	return 0;
}