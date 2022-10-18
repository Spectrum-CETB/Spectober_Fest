1. Max rectangle

Given a binary matrix M of size n X m. Find the maximum area of a rectangle formed only of 1s in the given matrix.

Problem Explanation:
Your task is to complete the function maxArea which returns the maximum size rectangle area in a binary-sub-matrix with all 1’s. The function takes 3 arguments the first argument is the Matrix M[ ] [ ] and the next two are two integers n and m which denotes the size of the matrix M.

Time Complexity:
 Time Complexity : O(n*m)
 Auixiliary Space : O(m) 


2.The Painter's Partition Problem-II

Dilpreet wants to paint his dog's home that has n boards with different lengths. The length of ith board is given by arr[i] where arr[] is an array of n integers. He hired k painters for this work and each painter takes 1 unit time to paint 1 unit of the board. 

The problem is to find the minimum time to get this job done if all painters start together with the constraint that any painter will only paint continuous boards, say boards numbered {2,3,4} or only board {1} or nothing but not boards {2,4,5}.

Problem Explanation:

Your task is to complete the function minTime() which takes the integers n and k and the array arr[] as input and returns the minimum time required to paint all partitions.

Time Complexity:

Time Complexity: O(n log m) , m = sum of all boards' length
Auxiliary Space: O(1)