#include <bits/stdc++.h>
using namespace std;


int main(){
  int n;
  cin>>n;
  int arr[n];
  for(int i=0;i<n;i++){
    cin >> arr[i];
  }
  int pivot;
  cin >> pivot;
  int prod = 1;

  //edge case
  if(pivot==0){
    for (int i = 0; i < n;i++){
      if(arr[i]==0){
        continue;
      }else{
        prod *= arr[i];
      }
    }
    cout << prod << endl;
    exit(0);
  }

  //normal case
  for(int i=0;i<n;i++){
    prod *= arr[i];
  }
  cout << prod / pivot << endl;
  return 0;
}
