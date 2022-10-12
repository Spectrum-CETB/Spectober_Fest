# 1. Problem Title - MAXIMUM_SUM
  Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Problem Explanation 🚀
We have to find the subarray with the largest sum possible in the array.

# Your logic 🤯
* Solved using kadane's Algorithm to find the maximum sum subarray in an integer array.

# Time Complexity and Space Complexity

```cpp
Time Complexity -> O(n)
Space Complexity -> O(1)

```

# 2. Problem Title: ANAGRAMS
Given two strings s and t we have to check if they are anagrams or not

# Problem Explanation 
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. e.g. 'anagrams' and 'nagarams' are anagrams but 'car' and 'rat' are not anagrams.

# Logic
* If two strings are to be anagrams then the first thing required is that they should be of equal length. If they are not of equal length then we return false
* Now we have ensured that both strings are of equal length, now they need to contain the same exact letters with the same exact frequency to be anagrams
* To check this we can create a frequency array of size 26(since the strings consist of only lowercase letters), and we can iterate through the string s and store the frequency of each letter in the frequency array.


# Time Complexity and Space Complexity
* Time Complexity: O(n)
* Space Complexity: O(1) 
