# 1. Anagrams

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Problem Explanation

We can consider two strings as anagrams, if they have the same characters, and each character occurs with the same frequency. Hence, the problem can be solved by maintaining the frequency of characters.

## My Logic

1. Read in the strings from input.
2. Created a boolean function named anagram.
3. Converted the strings to arrays of characters.
4. Sorted the characters in array.
5. If the arrays are equal then true else false.

## Test cases

1. Both are anagrams:
   - Input: s = "anagram" t = "nagaram"
   - Output: true

2. Both are not anagrams:

   - Input: s = "top" t = "cot"
   - Output: false

3. One is empty string:

   - Input: s = "hey" t = ""
   - Output: false

4. Both are empty strings:
   - Input: s = "" t = ""
   - Output: true


<!-- I don't know how to calculate time and space complexity-->

# 2. Majority Element

Given an array nums of size n, return the majority element.


## Problem Explanation

I have to print the majority element that appears more than ⌊n / 2⌋ times.

## My Logic

1. Taken the input as an integer l(the number of element in the array).
2. Created a array of the length l.
3. Used a for loop for taking inputs in the array.
4. Created a function majority element which returns majority element. Used nested for loop for searching majority element. Returned the majority element.
5. Printed the output.
6. As mentioned in the question that i may assume that the majority element always exists in the array, i didn't bother about n/2 criteria.

## Test cases

1. - Input: 3 [3,2,3]
   - Output: 3

2. - Input: 6 [1,5,1,6,1,9]
   - Output: 1
   
Time Complexity -> O(n^2) 

Space Complexity -> O(n)
