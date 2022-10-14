#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    //declaration of array and variables
    int a[10000];
    int i,j,n,d;
    int profit = 0;
    // no of days is  taken as input
    cin>>n;

    for ( i = 0; i < n; i++)
    {
        //value of stock on each day is taken as input 
        cin>>a[i];
    }


     //traversing thru the array to find out profits and finding maximum profit
    for ( i = 0; i < n; i++)
    {
        for ( j = i+1; j < n; j++)//here the comparison is from next day onwards cuz you must buy before u sell
        {
            if(a[i] <= a[j]){

                d=a[j] - a[i];
                //profit is compared with other profits and the greater profit is updated in profit variable
                if (d>profit)
                {
                
                    profit=d;
                }
                
                
            }

        }
        
    }
    //printing the  maximum profit out or if there is no profit printing 0
    cout<<profit;
    
    
    
}
