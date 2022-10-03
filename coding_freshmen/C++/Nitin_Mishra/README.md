# 1. Problem Title: Roman to Decimal
  Convert a string in Roman Numerals to Decimal System.

# Problem Explanation 🚀
A string of Roman Numerals is given, it is required to provide the output in the decimal system.

# Logic and Intuition 🧠
* An optimized approach will be to take an integer,initialised as zero,then the string is iterated through, decreasing or incerasing the values as needed, according the characters in the string.

# Time Complexity and Space Complexity
* Time Complexity: O(n)
* Space Complexity: O(1)

<br>
<hr>

# 2. Problem Title: Proficient Trader
  It is required to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Problem Explanation 🚀
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
For example: 
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Logic and Intuition 🧠
* We take two integers, one initialed as INT_MAX, to store the lowest the cost falls, another as 0 for the result.
* The array is iterated through,if the price is lower than the min value, we change the min value,
and if we are getting more profit than earlier at a certain price point, we update the answer value.

# Time Complexity and Space Complexity
* Time Complexity: O(n)
* Space Complexity: O(n)

# 3. Problem Title: Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Problem Explanation 🚀
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Logic and Intuition 🧠
* An efficient approach is to sort both input strings, if they match the string is an anagram.

# Time Complexity and Space Complexity
* Time Complexity: O(nlogn)
* Space Complexity: O(n)