#include <bits/stdc++.h>
using namespace std;

void search(string p, string t)
{
    int f = p.length();
    int s = t.length();
    for (int i = 0; i <= s - f; i++)
    {
        int j;
        for (j = 0; j < f; j++)
            if (t[i + j] != p[j])
                break;
        if (j == f)
            cout << "Pattern found at index " << i << endl;
    }
}

int main()
{
    string t;
    string p;
    cin >> t >> p;
    search(p, t);
    return 0;
}