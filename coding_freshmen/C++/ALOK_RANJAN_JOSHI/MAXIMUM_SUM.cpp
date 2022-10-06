#include <bits/stdc++.h>
using namespace std;

int maxSum(vector<int> &nums)
{
    int sum = nums[0], s = 0;
    for (auto val : nums)
    {
        s += val;
        sum = max(s, sum);
        if (s < 0)
            s = 0;
    }

    return sum;
}
int main()
{
    int n;
    vector<int> nums;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        nums.push_back(x);
    }
    cout << maxSum(nums) << endl;
}