#include<bits/stdc++.h>
using namespace std;

void test(){
    int n; cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    int len= sizeof(arr)/sizeof(arr[0]);
    int l =0, r =len-1;
 
    while (l < r)
    {
        while (arr[l]==0 && l<r){
            l++;
        }
        while (arr[r]==1 && l<r){
            r--;
        }
        if (l<r)
        {
            arr[l] = 0;
            arr[r] = 1;
            l++;
            r--;
        }
    }
    cout<<"After segregation:";
    for (int i=0; i<len; i++){
        cout<<arr[i]<<" ";
    }
}

int main(){
    int tc; cin>>tc;
    for(int i=1; i<=tc ;i++){
        //cout<<"CASE #"<<i<<":";
        test();
    }
    return 0;
}