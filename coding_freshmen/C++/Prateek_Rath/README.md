# 1. Majority Element
  Find the majority element in an array.

# Problem Explanation 🚀
A majority element is an element that appears more than n/2 times in the array, where n is the size of the array.

# Logic and Intuition
* An optimized approach will be to create a frequency array and store the frequency of each element that we iterate through the array, and finally check if the frequency of any element is greater than n/2 then that element is out majority element. The time complexity of this approach is O(n) and it has an additional space complexity of O(n) as well.
* This can be further optimized by using [Moore's Voting Algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm) which can solve the problem in constant space.
* In this algorithm we choose a candidate for majority element starting from the first element of the array, and we also initialize a count variable with 1.
* Then we start traversing the array and if the element encountered is same as the candidate element then we increase the count by 1 else we decrement the count by 1.
* If the count reaches 0 then we reset the candidate with the current element and reset the count to 1.
* Finally we return the candidate and if the array always has a majority element then the candidate will be the answer.

# Time Complexity and Space Complexity
* Time Complexity: O(n)
* Space Complexity: O(1)


# 2. Problem Title: SORT_01
  Sort an array consisting of 0s and 1s

# Problem Explanation 🚀
Basically we need to segregate the 1s and 0s so that all 0s are on the left side and all 1s are towards the right. 

# Intuition and Optimization🧠
* Basic brute force intuition that comes to mind at first is to sort the array, that way we can have all 0s on left and all 1s on right. But the time complexity in this case will be O(nlogn), which can definetely be optimized.
* We will follow a classic two pointer approact to solve this problem. One pointer always stays at 1s and another pointer moves forward. When the second pointer finds a 0 then it swaps with the 1 pointed to by the first pointer and both pointers move forward. We will continue this till we reach the end of the array.

# Time Complexity and Space Complexity
* Time Complexity: O(n)
* Space Complexity: O(1) --> Only two pointers required so thats constant extra space.
