#include <bits/stdc++.h>
using namespace std;
#define ll long long


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n;i++){
        cin >> arr[i];
    }
    int i = 0, j = 0;
    while(j<n){
        if(arr[j]==0){
            swap(arr[i], arr[j]);
            i++;
            j++;
        }else{
            j++;
        }
    }
    for (int i = 0; i < n;i++){
        cout << arr[i]<<" ";
    }
        return 0;
}