# 1. Problem Title: Maximum Sum
  Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
  (A subarray is a contiguous part of an array.)

# Problem Explanation 🚀
Here, the user gives input for n-size array and the elements for the array .
Then, we have to print out maximum sum possible from adding elements of contiguous subarray. 

# Logic and Intuition 🧠

* In the first iteration i divided the array into n number of subarray (n: number of elements in the array) and compared them with each other, the maximum integer gets stored in the max variable. In the second iteration, i have taken summation of 2 adjacent elements and compared them, the maximum summation gets stored in the max variable. In the third iteration, i have taken summation of 3 adjacent elements and compared them, the maximum summation gets stored in the max variable. And so on. 
* Here, i have taken two variables max and sum. "max" stores maximum sum of subarray found so far and second variable "sum" which stores summation of array elements into it as it iterates through the array.
* Everytime there is a sum value in "sum" compare it with "MAX" and update "MAX" if it is greater than "MAX" .

* TESTCASES:- 
  1) [-2,1,-3,4,-1,2,1,-5,4] --> 6
  2) [1,2,3,4,-7,4,8] --> 15

<!-- I don't know how to calculate time and space complexity-->
