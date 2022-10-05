# MAJORITY_ELEMENT
Given an array nums of size n, return the majority element.

# Problem Explanation 🚀
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# My logic 🤯
My approach was to first make a set of the array to avoid counting the same element multiple times and then counting the number of occurances of the set elements. If the count is more than half the length of the array then we return the element of the array.
 
 TEST CASES:
 1. input: [3,2,3]
    output: 3

 2. input: [4,2,2,2,2,5,4]
    output: 2

 3. input: [-1,2,0,0,-1,4,0,6,0,0]
    output: none (as none of the elements' count is greater than n/2)

# Time Complexity and Space Complexity
```python

Time Complexity -> O(n)
Space Complexity -> O(1)

```    