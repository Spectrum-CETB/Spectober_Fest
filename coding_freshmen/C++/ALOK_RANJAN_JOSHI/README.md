# 1. Problem Title: Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Problem Explanation

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Logic and Intuition

- Here the logic i applied is to sort both the striings and compare both strings.

# Time Complexity and Space Complexity

- Time Complexity: O(n logn)
- Space Complexity: O(1)
<hr>

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
