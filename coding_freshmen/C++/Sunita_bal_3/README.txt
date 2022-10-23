1.Trapping Rain Water

Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

Problem Explanation:
You don't need to read input or print anything. The task is to complete the function trappingWater() which takes arr[] and N as input parameters and returns the total amount of water that can be trapped.

Time Complexity:
Time Complexity: O(N)
Auxiliary Space: O(N)


2.Allocate minimum number of pages

You are given N number of books. Every ith book has Ai number of pages. The books are arranged in ascending order.

You have to allocate contiguous books to M number of students. There can be many ways or permutations to do so. In each permutation, one of the M students will be allocated the maximum number of pages. Out of all these permutations, the task is to find that particular permutation in which the maximum number of pages allocated to a student is the minimum of those in all the other permutations and print this minimum value.

Each book will be allocated to exactly one student. Each student has to be allocated at least one book.

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).

Problem Explanation:
You don't need to read input or print anything. Your task is to complete the function findPages() which takes 2 Integers N, and m and an array A[] of length N as input and returns the expected answer.

Time Complexity:
Time Complexity: O(NlogN)
Auxilliary Space: O(1)
