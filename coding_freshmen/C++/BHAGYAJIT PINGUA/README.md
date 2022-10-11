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
  
# Problem Title: PATTERN_FINDER
  Given a text txt[0. . .n-1] and a pattern pat[0. . .m-1].
write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[].
You may assume that n > m.

# Problem Explanation 🚀
  Here the user inputs two strings, one of the string is very very larger in size than the other one. The objective is to find the number of times the smaller string appears in the larger string.
  
# Logic and Intuition
  Here, the approach is that the the user inputs two strings, then the length of the two string is first found, then a loop executes n(length of txt) times and inside that loop there's another loop that executes m(length of pat) times, and checks the number of times pat appears in txt, a counter variable updates, if it is equal to m then the index position at which the pattern is found in the text is printed.
  
  
 TESTCASE:-
1. 
ABABABBBBBABABBBBABBBBBBB
AB
Patten found at index 0
Patten found at index 2
Patten found at index 4
Patten found at index 10
Patten found at index 12
Patten found at index 17

2.
ajv avavqaujhv qqbvqaefvbqa
 ava
Patten found at index 3

# Time Complexity and Space Complexity
  Time complexity:-O(n*n)
  Space Complexity:-O(n)
