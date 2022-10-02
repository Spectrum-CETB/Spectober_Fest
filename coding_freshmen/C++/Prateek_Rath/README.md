# Problem Title: SORT_01
  Sort an array consisting of 0s and 1s

# Problem Explanation 🚀
Basically we need to segregate the 1s and 0s so that all 0s are on the left side and all 1s are towards the right. 

# Intuition and Optimization🧠
* Basic brute force intuition that comes to mind at first is to sort the array, that way we can have all 0s on left and all 1s on right. But the time complexity in this case will be O(nlogn), which can definetely be optimized.
* We will follow a classic two pointer approact to solve this problem. One pointer always stays at 1s and another pointer moves forward. When the second pointer finds a 0 then it swaps with the 1 pointed to by the first pointer and both pointers move forward. We will continue this till we reach the end of the array.

# Time Complexity and Space Complexity
* Time Complexity: O(n)
* Space Complexity: O(1) --> Only two pointers required so thats constant extra space.
