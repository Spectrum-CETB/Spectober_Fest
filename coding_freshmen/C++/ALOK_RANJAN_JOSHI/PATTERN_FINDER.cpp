#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    string txt, pat;
    cin >> txt >> pat;
    ll n = txt.length(), m = pat.length();
    transform(txt.begin(), txt.end(), txt.begin(), ::tolower);
    transform(pat.begin(), pat.end(), pat.begin(), ::tolower);
    char s1[n + 1], s2[m + 1];
    pat.copy(s2, m);
    s2[m] = '\0';
    cout << s2 << endl
         << endl;

    for (ll i = 0; i <= n - m; i++)
    {
        txt.copy(s1, m, i);
        s1[m] = '\0';
        if (strcmp(s1, s2) == 0)
            cout << "Pattern found at index " << i << endl;
    }
}