# function declaration to find the majority element
def majority_element(arr,n):

    for i in set(arr):                 # set is used to count an element once 
        if (arr.count(i)) > (n//2):     # if count of an element is greater than n/2 return the corresponding element
            print(i)
                
# input an array of single spaced integers
nums = list(map(int,input().split()))
n = len(nums) # n is the length of array
majority_element(nums,n)