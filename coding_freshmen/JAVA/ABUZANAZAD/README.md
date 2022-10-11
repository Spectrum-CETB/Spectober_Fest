```
# SORT_01
  Q : You are given an array of 0s and 1s in random order.

  Segregate 0s on left side and 1s on right side of the array [Basically you have to sort the array]. 

  Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 

  Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 

# Problem Explanation 🚀
It is a sorting of an array in ascending order

# Your logic 🤯
* I used the Java util package for it Scanner class for input and Arrays.sort method to sort the array in ascending order.
* Own test cases if any:
*     Input array: [0,1,0,1,1,0,0]
*     Output array: [0, 0, 0, 0, 1, 1, 1]

// Time Complexity: O(N log N)
// Auxiliary Space: O(1)

```
```
# ROMAN_TO_DECIMAL
  Q : Given a roman numeral, convert it to an integer.

    Input: s = "III"
    Output: 3
    Explanation: III = 3

    Constraints:

    1 <= s.length <= 10
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

# Problem Explanation 🚀
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

# Your logic 🤯
* I used two static array to act as a map for each number with its roman number representation. Then as per roman number, summed the corresponding decimal values. When ever a I, X, L is encountered bebore V,L,D then the sum is substracted with the twice of the I,X,L encountered.

* Own test cases if any:
*     Input: xiv
*     Output: Integer = 14



```
