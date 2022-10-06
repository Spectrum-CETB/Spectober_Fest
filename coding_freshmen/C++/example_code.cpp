/*sort_01*/
#include<iostream>
using namespace std;
void seg 0 and 1(int arr[100],int n)
{
	int count=0;
	for(int i=0;i<n;i++)
	{
		if(arr[i]==0)
		count++;
	}
	for(int i=0;i<count;i++)
	{
		arr[i]=0;
	}
	for(int i=count;i<n;i++)
	{
		arr[i]=1;
	}
}
void printarray(int arr[100],int n)
{
	cout<<"new array is";
	for(int i=0;i<n;i++)
	cout<<arr[i]<<" ";
}
int main()
{
	int arr[100],n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	seg 0 and 1(int arr[n],int n);
	printarray(arr,n);
	return 0;
}
