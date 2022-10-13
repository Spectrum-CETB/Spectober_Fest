#include <bits/stdc++.h>
using namespace std;
int roman_to_int(string s)
{
    map<char, int> m = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};

    int t = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (m[s[i + 1]] <= m[s[i]])
            t += m[s[i]];
        else
            t -= m[s[i]];
    }
    return t;
}
int main()
{
    string s;
    cout << "s =";
    getline(cin, s);
    int n;
    n = roman_to_int(s);
    cout << n;
    return 0;
}
