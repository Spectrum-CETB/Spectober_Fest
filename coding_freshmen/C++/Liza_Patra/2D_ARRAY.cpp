#include <bits/stdc++.h>
using namespace std;
void sum(vector<vector<int>> &mt, int t)
{
    if (mt.size() == 0)
    {
        cout << 0 << endl;
        return;
    }

    int m = mt.size();
    int n = mt[0].size();

    int sum = 0;

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (mt[i][j] != t)
                sum += mt[i][j];
            else
            {
                cout << sum << endl;
                return;
            }
        }
    }
    cout << sum << endl;
}
int main()
{
    int r, c;
    cin >> r >> c;
    vector<vector<int>> mt(r);
    for (int i = 0; i < r; i++)
    {
        mt[i] = vector<int>(c);
        for (int j = 0; j < c; j++)
            cin >> mt[i][j];
    }
    int t;
    cin >> t;
    sum(mt, t);

    return 0;
}