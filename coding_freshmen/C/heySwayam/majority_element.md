# <Title of the Problem>
Majority Element

# Problem Explanation 🚀
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Your logic 🤯
* Approach: 
--> Count of frequency of each element of array using two for loop.
--> Outer for loop will fix one element(let's say K) and inner for loop will count the occurrences of K in inputArray.
--> If count of K is more than N/2 then K is a majority element.
--> If we don't find any element whose count is > N/2 then inputArray doesn't contain any majority element.
* Own test cases if any
* Code Structure and Libraries used

# Time Complexity and Space Complexity
```cpp
Example 

Time Complexity -> O(n^2)
Space Complexity -> O(1)

```