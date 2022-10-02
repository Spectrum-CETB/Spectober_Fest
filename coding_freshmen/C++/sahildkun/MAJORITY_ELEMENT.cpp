#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    //array and variable declaration
    int a[100];
    int i,j,n;
    int count=0;

    //array length or size input
    cin>>n;

    //array elements input
    for ( i = 0; i < n; i++)
    {
        cin>>a[i];
    }

    //operation on array for finding majority element
    //using two loops ...one for traversing thru the array and other for comparison
    for ( i = 0; i < n; i++){
      
        count=0;
        for ( j = i+1; j < n; j++){
          
          //comparison between different array elements
             if (a[i] == a[j])
            {
                count++;//updating the count the no of times comparison staisfies
                
                if ((count+1)>n/2)//conditon of the majority element in array
               {
                 cout<<a[i]<<endl;//majority elemnt output
                 break;
               }
            }
        }
    }

}
