
#include <bits/stdc++.h>
using namespace std;

int maxSubArray(vector<int> &nums)
{
    int sum = nums[0], s = 0;
    for (auto val : nums)
    {
        s += val;
        if (s > sum)
            sum = s;
        if (s < 0)
            s = 0;
    }

    return sum;
}
int main()
{
    vector<int> numbers;
    int n;
    cin >> n;
    while (n--)
    {
        int x;
        cin >> x;
        numbers.push_back(x);
    }
    cout << maxSubArray(numbers) << endl;
    return 0;
}