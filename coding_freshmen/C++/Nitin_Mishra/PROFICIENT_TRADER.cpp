#include <bits/stdc++.h>
using namespace std;
int solution(vector<int>& prices) {
        int mxn = INT_MAX;
        int ans = 0;
        for(int i = 0; i < prices.size(); i++){
            if(prices[i] < mxn){
                mxn = prices[i];
            }else if(prices[i] - mxn > ans){
                ans = prices[i] - mxn;
            }
        }
        return ans;
    }
int main()
{
	int n;
    cin>>n;
    vector<int> test(n);
    for(int i=0;i<n;i++)
	    cin >> test[i];
	cout<<solution(test)<<endl;
	return 0;
}