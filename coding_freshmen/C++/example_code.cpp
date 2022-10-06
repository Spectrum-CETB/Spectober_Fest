/*majority element*/
#include<iostream>
using namespace std;
void majorityele(int arr[],int n)
{ 
	int mcount =0;
	int index=-1;
	for(int i=0;i<n;i++)
	{
            int count =0;
		for(j=0;j<n;j++)
		{
			if(arr[i]==arr[j])
				count++;
		}
	
if(count>mcount)
{
	mcount=count;
	index =i;
}
}
if(mcount>n/2)
	cout<<arr[index]<<endl;
	else
		cout<<" majority element not found"<<endl;
}
int main()
{
	int arr[100],n,i;
	cin>>n;
	for(i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	majorityele(arr[],n);
	return 0;
}
