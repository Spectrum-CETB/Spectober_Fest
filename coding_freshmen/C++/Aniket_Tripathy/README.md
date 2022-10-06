# 1. Problem Title: PRODUCT_FINDER
  Find the product of the elements of the array except the given pivot element

# Problem Explanation 🚀
We need to find the product of all elements of the array while skipping the pivot element 

# Intuition and Logic🧠
*  Assuming that all the elements in the array are unique we can simply calculate the products of all the elements in a prod variable, and when we encounter the pivot element we can simply use the continue; statememt to skip that element.

# Time Complexity and Space Complexity
* Time Complexity: O(n)
* Space Complexity: O(1)


# 2. Problem Title: ANAGRAMS
Given two strings s and t we have to check if they are anagrams or not

# Problem Explanation 
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. e.g. 'anagrams' and 'nagarams' are anagrams but 'car' and 'rat' are not anagrams.

# Intuition and Logic🧠
* If two strings are to be anagrams then the first thing required is that they should be of equal length. If they are not of equal length then we return false
* Now we have ensured that both strings are of equal length, now they need to contain the same exact letters with the same exact frequency to be anagrams
* To check this we can create a frequency array of size 26(since the strings consist of only lowercase letters), and we can iterate through the string s and store the frequency of each letter in the frequency array.
* Now we iterate through string t and keep checking if each letter in t is present in the frequency array or not, if the letter is present(i.e. frequency is greater than 0) then we decrease the frequency by 1. 
* In case we find than the frequency of a letter in the array is 0 then that implies that the letter is present in string t but not in string s so that means that out strings are not anagrams and we return false
* Else if all checks are passed, our strings are anagrams and we return true.

# Time Complexity and Space Complexity
* Time Complexity: O(n)
* Space Complexity: O(1) --> Since an constant space array of size 26 is used
