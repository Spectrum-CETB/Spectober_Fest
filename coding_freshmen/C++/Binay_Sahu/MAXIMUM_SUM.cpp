#include <bits/stdc++.h>
using namespace std;
#define ll long long;


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    //kadene's algo
    int mx = 0;
    int curr = 0;
    for(int i=0;i<n;i++){
        if(curr+arr[i]>arr[i]){
            curr += arr[i];
            mx = max(mx, curr);
        }else{
            curr = arr[i];
        }
    }
    cout << mx << endl;
    return 0;
}
/* 
9
-2 1 -3 4 -1 2 1 -5 4
test case passed
*/