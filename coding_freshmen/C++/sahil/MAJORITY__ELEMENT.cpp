#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int a[100];
    int i,j,n;
    int count=0;
    cin>>n;

    for ( i = 0; i < n; i++)
    {
        
        cin>>a[i];
    }
    
      for ( i = 0; i < n; i++)
      {
        count=0;
        for ( j = i+1; j < n; j++)
        {
            
            if (a[i] == a[j])
            {
                count++;
                if ((count+1)>n/2)
               {
                 cout<<a[i]<<endl;
                 break;
               }

            }
        }
    }

}
