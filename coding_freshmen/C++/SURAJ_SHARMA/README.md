1.Clone a linked list with next and random pointer	
You are given a special linked list with N nodes where each node has a next pointer pointing to its next node. You are also given M random pointers, where you will be given M number of pairs denoting two nodes a and b  i.e. a->arb = b.

Construct a copy of the given list. The copy should consist of exactly N new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

Problem Explanation:
The task is to complete the function copyList() which takes one argument the head of the linked list to be cloned and should return the head of the cloned linked list.

Algorithm and Logic:

>Create the copy of node 1 and insert it between node 1 & node 2 in the original Linked List, create a copy of 2 and insert it between 2 & 3. Continue in this fashion, add the copy of N after the Nth node 
>Now copy the random link in this fashion 
>This works because original->next is nothing but a copy of the original and Original->random->next is nothing but a copy of the random. 
>Now restore the original and copy linked lists in this fashion in a single loop. 
>Ensure that original->next is NULL and return the cloned list

Time Complexity and Space Complexity:
Time Complexity : O(n)
Auxilliary Space : O(1)

2.Allocate minimum number of pages
You are given N number of books. Every ith book has Ai number of pages. The books are arranged in ascending order.

You have to allocate contiguous books to M number of students. There can be many ways or permutations to do so. In each permutation, one of the M students will be allocated the maximum number of pages. Out of all these permutations, the task is to find that particular permutation in which the maximum number of pages allocated to a student is the minimum of those in all the other permutations and print this minimum value.

Each book will be allocated to exactly one student. Each student has to be allocated at least one book.

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).

Problem Explanation:
Your task is to complete the function findPages() which takes 2 Integers N, and m and an array A[] of length N as input and returns the expected answer.

Algorithm and Logic:
>Initialise the start to minimum(pages[]) and end = sum of pages[],
>Do while start <= end
  >Calculate the mid and check if mid number of pages can assign any student by satisfying the given condition such that all students will get at least one book. Follow the steps to check for validity.
  >Initialise the studentsRequired = 1 and curr_sum = 0 for sum of consecutive pages of book
  >Iterate over all books or say pages[]
    >Add the pages to curr_sum and check curr_sum > curr_min then increment the count of studentRequired by 1.
    >Check if the studentRequired > M, return false.
    >Return true.
  >If mid is valid then, update the result and move the end = mid – 1
  >Otherwise, move the start = mid + 1
>Finally, return the result.

Time Complexity and Space Complexity:
Time Complexity: O(NlogN)
Auxilliary Space: O(1)

3.Count Inversions
Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Problem Explanation:
Your task is to complete the function inversionCount() which takes the array arr[] and the size of the array as inputs and returns the inversion count of the given array.

Logic:
Use Merge sort with modification that every time an unsorted pair is found increment count by one and return count at the end.

Time Complexity and Space Complexity:
Time Complexity: O(NLogN).
Auxiliary Space: O(N).




