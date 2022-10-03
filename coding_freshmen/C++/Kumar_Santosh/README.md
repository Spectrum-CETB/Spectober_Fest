# 1. Problem Title: Maximum Sum
  Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
  (A subarray is a contiguous part of an array.)

# Problem Explanation 🚀
Here, the user gives input for n-size array and the elements for the array .
Then, we have to print out maximum sum possible from adding elements of contiguous subarray. 

# Logic and Intuition 🧠
* Here, the basic approach I have applied is also known as Kedane's Algorithm in which I have taken two variables MAXsum
  which stores the maximum sum of subarray found so far and second variable "sum" which stores summation of array elements into it as it 
  iterates through the array.
* Everytime there is a positive-sum value in "sum" compare it with "MAXsum" and update "MAXsum" if it is greater than "MAXsum" .
* And if there is a negative-sum value(<0) in "sum" and then it changes the value into 0.

* TESTCASES:- 
  1) [-2,1,-3,4,-1,2,1,-5,4] --> 6
  2) [1,2,3,4,-7,4,8] --> 15

# Time Complexity and Space Complexity
* Time Complexity: O(n)
* Space Complexity: O(1)

