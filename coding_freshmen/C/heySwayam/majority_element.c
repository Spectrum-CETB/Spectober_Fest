#include <stdio.h>
#include <string.h>
int main(){
    int num[100];
    int len,n=0;
    printf("Enter the lenth of array: ");
    scanf("%d",&len);
    // getting inputs for arrays
    for (int i = 0; i < len; i++)
    {
        printf("Enter element-%d :",i+1);
        scanf("%d",&num[i]);
    }
    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < len; j++)
        {
            if (num[i]==num[j])
            {
                n++;
            }
            
        }
        if (n>len/2)
        {
            printf("The majority element: %d",num[i]);
            break;
        }
        
    }
    
    return 0;
}