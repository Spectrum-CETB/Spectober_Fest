# Anagrams

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
