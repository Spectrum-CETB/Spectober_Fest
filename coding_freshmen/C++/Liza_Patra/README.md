# <Title of the Problem>

Given a roman numeral, convert it to an integer.
Input: s = "III"
Output: 3
Explanation: III = 3

# Problem Explanation 🚀

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
In order to solve this problem, I needed to first understand how to read roman numerals and translate them my hand.

# Your logic 🤯

- 1.(ADDING) The value of each symbol is (generally) added together from left to right:
  MMLVII (1,000+1,000+50+5+1+1) = 2,057 2. (SUBTRACTING) When there is a smaller number placed before a larger number
  XIX (10 + (10 − 1)) = 19

# Time Complexity and Space Complexity

Time Complexity -> O(n)
Space Complexity -> O(n)

# 2.Title of the Problem:Sort_array

You are given an array of 0s and 1s in random order.

# Problem Explanation 🚀

Segregate 0s on left side and 1s on right side of the array [Basically you have to sort the array].
Input array = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
Output array = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# Your logic 🤯

- simply we have to sorting the array in ascending order.

# Time Complexity and Space Complexity

Time Complexity -> O(n logn)
Space Complexity -> O(n)

# 4.Title of the Problem:2D_ARRAY_SUM

\*Write an efficient algorithm that returns sum upto a value target in an m x n integer matrix . This matrix has the following properties:

# Problem Explanation 🚀

\*Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 10
Output: 15
Explanation : 1+3+5+7 = 16

# Your logic 🤯

# Time Complexity and Space Complexity

Time Complexity -> O(n^2)
Space Complexity -> O(n^2)
