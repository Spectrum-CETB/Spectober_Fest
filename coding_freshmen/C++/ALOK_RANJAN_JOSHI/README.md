# 1. Problem Title: Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Problem Explanation

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Logic and Intuition

- Here the logic i applied is to sort both the striings and compare both strings.

# Time Complexity and Space Complexity

- Time Complexity: O(n logn)
- Space Complexity: O(1)

# 2. Problem Title: PATTERN_FINDER

Given a text txt[0. . .n-1] and a pattern pat[0. . .m-1].

# Problem Explanation

write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[].
You may assume that n > m.

# Logic and Intuition

- Here the logic that i applied is to copy a part of txt string of length equal to pat string to another variable. Then this variable is compared to the string pat, if they are equal then print the msg, oterwise continue the loop. The loop continue to the index (n - m) of txt string.

# Time Complexity and Space Complexity

- Time Complexity: O(n^2)
- Space Complexity: O(n)

# 3. Problem Title: ROMAN_TO_INTEGER

Given a roman numeral, convert it to an integer. Input: s = "III" Output: 3 Explanation: III = 3

# Problem Explanation

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999. In order to solve this problem, I needed to first understand how to read roman numerals and translate them my hand.

# Logic and Intuition

- Here the logic that i applied is that is the value of roman alphabet of any position is lesser than it's immediate right position then it has to be added oterwise it has to be subtracted.

# Time Complexity and Space Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

# 4. Problem Title: MAXIMUM_SUM

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Problem Explanation

A subarray is a contiguous part of an array.

# Logic and Intuition

- Here the logic that i applied is to add the numbers from starting index, if it's found greater than the sum then this value will be assigned to the sum, if the addition value become negative, then it's made 0.
# Time Complexity and Space Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)
