# Problem Title: ANAGRAMS
  Given two strings s and t, return true if t is an anagram of s, and false otherwise.
  An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
  
# Problem Explanation 🚀
 Here, the user inputs two strings, if letters of one of the string if rearranged, forms the other string then the output is true else false.


# Logic and Intuition
  Here, the approach is that the the user inputs two strings, then the length of the two string is first found if their lengths are equal then each letter of one string is checked with each letter of  the other string.
  A counter variable counts the number of times each letter of one string is equal with the letter of the other string.
  Finally If the counter variable is equal to the length of the string then program returns true, else false.
  
  TESTCASES:-
  1. s=rat
     t=art
     true
     
  2.s=anagram
    t=nagramm
    false
    
# Time Complexity and Space Complexity
  Time complexity:-O(n*n)
  Space Complexity:-O(n)
  
