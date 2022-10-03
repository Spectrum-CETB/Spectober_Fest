#include <bits/stdc++.h>
using namespace std;
long long int solution(vector<int>& arr,int n,int k) {
        long long int prod = 1;
        bool found= false;
        for(int i = 0; i < n; i++){
            if(arr[i] == k && !found){
                found=true;
            }else {
                prod=prod*arr[i];
            }
        }
        return prod;
    }
int main()
{
	int n;
    cin>>n;
    vector<int> test(n);
    for(int i=0;i<n;i++)
	    cin >> test[i];
    int k;
    cin>>k;
	cout<<solution(test,n,k)<<endl;
	return 0;
}