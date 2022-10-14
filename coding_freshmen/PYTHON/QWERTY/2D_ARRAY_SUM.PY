# Get the size m and n
M = 4
N = 4
 
# Function to calculate sum
# of elements in 2d array
def sum(arr):
 
    sum = 0
 
    # Finding the sum
    for i in range(M):
        for j in range(N):
           
            # Add the element
            sum = sum + arr[i][j]
 
    return sum
 