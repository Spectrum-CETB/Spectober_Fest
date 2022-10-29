# <Title of the Problem>
Given an array nums of size n, return the majority element.

# Problem Explanation 🚀
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Your logic 🤯
Approach: Initialize count with zero. Initialize max with first element of array and increment count by 1. Now, if next element is equal to max, increment the count by 1, else decrement. Whenever the count becomes zero, element at that index in array traversal is assigned to max and same procedure is followed.


# Time Complexity and Space Complexity
Time Complexity -> O(n)
Space Complexity -> O(1)