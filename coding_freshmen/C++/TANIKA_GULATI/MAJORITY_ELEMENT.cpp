#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int nums[n];
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }
    int max;
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        if (count == 0)
        {
            max = nums[i];
            count = 1;
            continue;
        }
        if (max != nums[i])
        {
            count--;
        }
        else
        {
            count++;
        }
    }
    cout << max;
}
