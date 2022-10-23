#include<stdio.h>
#include<stdlib.h>

void heapify(int A[],int i,int size){
    int left = 2*i+1 , right = 2*i+2  , largest = i  , temp;

    if(left <size && A[left]>A[largest]) largest = left;
    if(right <size && A[right]>A[largest]) largest = right;

    if(largest!=i) {
        temp = A[i];
        A[i] = A[largest];
        A[largest] = temp;
        heapify(A,largest,size);
    }

}

void build_max_heap(int A[],int size) {
    int i;
    for(i=size/2-1;i>=0;i--) heapify(A,i,size);    
}

int main()
{
    int n , A[100] , i , j ,temp,size,counter=0;

    printf("Enter the size of the arrray :");
    scanf("%d", &n);

    size = n;

    printf("Enter the elements of the array :");
    for(i=0;i<n;i++) scanf("%d", &A[i]);

    // build max heap
    build_max_heap(A,size);

    // procedure for heap
    for(i=n-1;i>0;i--){
        // first step -> swap
        temp = A[0];
        A[0] = A[i];
        A[i] = temp;

        // again call heapaify with size - 1;
        build_max_heap(A,i);
    }

    printf("The sorted array is :");
    for(i=0;i<n;i++) printf("%d ",A[i]); 
    return 0;
}
