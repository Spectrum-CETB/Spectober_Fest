#include <bits/stdc++.h>
using namespace std;
void SioErato(int n) // Sieve of Eratosthenes
{
    int i;
    bool t[n + 1];
    fill(t, t + n + 1, true);
    t[0] = false, t[1] = false;
    for (i = 2; i * i <= n; i++)
        if(t[j])
            for (int j = 2 * i; j <= n; j += i)
                if (j % i == 0)
                    t[j] = false;
                    
    for (i = 1; i <= n; i++)
        if (t[i] == true)
            cout << i << " ";
}
int main()
{
    int n;
    cout<<"Enter upper limit: ";
    // cin>>n;
    SioErato(1000);
    return 0;
}
