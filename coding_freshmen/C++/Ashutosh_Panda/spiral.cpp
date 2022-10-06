#include<bits/stdc++.h>
using namespace std;
void spiOrd(vector<vector<int>> &m)
{
    int i, l = 0, u = 0, d = m.size(), r = m[0].size();
    while (l < r and u < d)
    {
        for (i = l; i < r; i++)
            cout<<m[u][i]<<" ";
        u++;
        for (i = u; i < d; i++)
            cout<<m[i][r - 1]<<" ";
        r--;
        if (u < d)
        {
            for (i = r - 1; i >= l; i--)
                cout<<m[d - 1][i]<<" ";
            d--;
        }
        if (l < r)
        {
            for (i = d - 1; i >= u; i--)
                cout<<m[i][l]<<" ";
            l++;
        }
    }
}

int main()
{
    int n,r,c,i,j;
    cout<<"enter no. of rows and columns: ";
    cin>>r>>c;
    vector<vector<int>>v(r,vector<int>(c,0));
    for(i=0;i<r;i++)
        for(j=0;j<c;j++)
            cin>>v[i][j];
    spiOrd(v);
    return 0;
}