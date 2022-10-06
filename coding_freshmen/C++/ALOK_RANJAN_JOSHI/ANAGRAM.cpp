#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s1, s2;
    cin >> s1 >> s2;
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    cout << (s1 == s2 ? "true" : "false") << endl;

    return 0;
}

//It's code by ALOK RANJAN JOSHI