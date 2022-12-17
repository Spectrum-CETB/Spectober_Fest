#include <iostream>
using namespace std;
 
// Get the size m and n
#define M 4
#define N 4
 
// Function to calculate sum
// of elements in 2d array
int sum(int arr[M][N])
{
    int i, j;
    int sum = 0;
 
    // Finding the sum
    for (i = 0; i < M; ++i) {
        for (j = 0; j < N; ++j) {
            // Add the element
            sum = sum + arr[i][j];
        }
    }
    return sum;
}
 
// Driver code
int main()
{
    int i, j;
    int arr[M][N];
 
    // Get the matrix elements
    int x = 1;
    for (i = 0; i < M; i++)
        for (j = 0; j < N; j++)
            arr[i][j] = x++;
 
    // Get sum
    cout << sum(arr);
    return 0;
}
