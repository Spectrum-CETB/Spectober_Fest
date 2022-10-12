// #include <bits/stdc++.h>
// using namespace std;
// long long int find(long long int *p, long long int n, long long int val)
// {
//     for (long long int i = 0; i < n; i++)
//     {
//         if (p[i] == val)
//             return i;
//     }
// }
// int main()
// {
//     long long int t;
//     cin >> t;
//     while (t--)
//     {
//         long long int n, count = 0; // trainers
//         cin >> n;
//         long long int pg[n], pw[n], decg[n], decw[n], i, j;
//         for (i = 0; i < n; i++)
//             cin >> pg[i];
//         for (i = 0; i < n; i++)
//             cin >> pw[i];
//         for (i = 0; i < n; i++)
//         {
//             auto it = max_element(pg, pg + n);
//             decg[i] = it - pg;
//             *it = 0;
//             it = max_element(pw, pw + n);
//             decw[i] = it - pw;
//             *it = 0;
//         }
//         for (i = 0; i < n; i++)
//         {
//             auto val = decg[i];
//             auto check = 1;
//             auto indexvalw = find(decw, n, val);
//             for (j = 0; j < i; j++)
//             {
//                 auto indexw = find(decw, n, decg[j]);
//                 if (indexvalw > indexw)
//                 {
//                     check = 0;
//                     break;
//                 }
//             }
//             if (check == 1)
//                 count++;
//         }
//         cout << count << endl;
//     }

//     return 0;
// }

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