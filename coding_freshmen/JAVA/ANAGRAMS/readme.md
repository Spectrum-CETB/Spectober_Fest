# Anagrams

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Problem Explanation

We can consider two strings as anagrams, if they have the same characters, and each character occurs with the same frequency. Hence, the problem can be solved by maintaining the frequency of characters.

## My Logic

1. Read in the strings from input
2. If the strings are of different length:
    1. Return false and exit (Cannot be an anagram)
3. For each string do:
    1. For each character in the string, store the frequency of the character in a dictionary.
4. If the dictionaries are different:
    1. Return false and exit.
5. Return true

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

## Time Complexity

The program has one for loop, and one dictionary iteration:

1. The first for loop, loops over the entire two strings. Taking the strings combined length as N, it is O(N)
2. The dictionary iteration may be up to O(len_dict_1+len_dict2). In the worst case, this would be O(N) (if all characters are unique)

Total complexity is O(N) + O(N) = O(N)

Hence, the time complexity is O(N).

## Space Complexity

The program would use a dictionary to store the characters. A dictionary would use approximately O(1) space per character. There may be N unique characters, hence the space used would be O(N*1).

Total space complexity is O(N)
