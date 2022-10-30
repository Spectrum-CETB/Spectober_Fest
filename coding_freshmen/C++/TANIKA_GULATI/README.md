# Problem 1: MAJORITY_ELEMENT
Given an array nums of size n, return the majority element.

# Problem Explanation 🚀
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Your logic 🤯
Approach: Initialize count with zero. Initialize max with first element of array and increment count by 1. Now, if next element is equal to max, increment the count by 1, else decrement. Whenever the count becomes zero, element at that index in array traversal is assigned to max and same procedure is followed.

# Time Complexity and Space Complexity
Time Complexity -> O(n)
Space Complexity -> O(1)


# Problem 2: SORT_01
You are given an array of 0s and 1s in random order. Sort the array.

# Problem Explanation 🚀
Segregate 0s on left side and 1s on right side of the array.

# Your logic 🤯
Approach: Initialize start and end positions of the array. Increment start if array element at start is 0. If it is 1, swap the elements at start and end, and decrement end by 1. Repeat the steps until start is less than end.

# Time Complexity and Space Complexity
Time Complexity -> O(n)
Space Complexity -> O(1)