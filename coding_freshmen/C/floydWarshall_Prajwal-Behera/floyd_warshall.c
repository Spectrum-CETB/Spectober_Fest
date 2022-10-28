#include<stdio.h>
#include<stdlib.h>

#define MAX 9999

int min(int x,int y){
    return x<=y ? x:y;
}

int main(){
    int n , m;
    int u , v , w;
    int i , j , k;
    int prev[20][20] , curr[20][20];

    printf("Enter the number of vertices :");
    scanf("%d",&n);

    printf("Enter the number of edges :");
    scanf("%d",&m);

    // initialization
    for(i=0;i<20;i++){
        for(j=0;j<20;j++){
            if(i==j) prev[i][j] = 0;
            else prev[i][j] = MAX;
        }
    }

    for(i=0;i<m;i++)
    {
        printf("Enter the edge -> edge and its weight :");
        scanf("%d %d %d",&u,&v,&w);
        prev[u][v] = w;
    }   

    // d0 = prev

    for(k=1;k<=n;k++){

        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                if(i==k || j==k || i==j) curr[i][j] = prev[i][j];
                else {
                    curr[i][j] = min(prev[i][j] , prev[i][k] + prev[k][j]);
                }
            }
        }

        // curr is perfectly updated
        // now set curr to prev

        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                prev[i][j] = curr[i][j];
            }
        }
    }

    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++) printf("%d ",prev[i][j]);
        printf("\n");
    } 

    return 0;
}