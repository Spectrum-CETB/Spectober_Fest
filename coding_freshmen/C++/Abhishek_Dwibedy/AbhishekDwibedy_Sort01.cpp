#include<bits/stdc++.h>
using namespace std;


void sort(int arr[], int n)
{
    int j = -1;
    for (int i = 0; i < n; i++) {
 
        // if number is smaller than 1 then swap it with j-th number
        if (arr[i] < 1) {
            j++;
            swap(arr[i], arr[j]);
        }
    }
}


int main(){
    int size;
    cin>>size;
    int array[size];
    for (int i = 0; i < size; i++)
    {
        cin>>array[i];
    }
    sort(array,size);
    for (int i = 0; i < size; i++)
    {
        cout<<array[i]<<" ";
    }
    cout<<endl;
    return 0;
}   


