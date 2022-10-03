<h1>PIVOT_SUM</h1>
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

# Problem Explanation 🚀
If Input: arr = [1,7,3,6,5,6]
<br>
Output: 3
<br>
Explanation:
The pivot index is 3. 
<br>Left sum = arr[0] + arr[1] + arr[2] = 1 + 7 + 3 = 11
<br>Right sum = arr[4] + arr[5] = 5 + 6 = 11

# My logic 🤯
### Approach
My approach is to find the total sum of all elements and then traversing the array while adding the specific element I traverse and substracting the total sum traversed to check if both sides have equal sum. Else printing -1 is no such element satisfies this. 

<h3>Test Cases</h3>

1. Pivot element is present:
   - Input: 1 2 3 4 6
   - Output: 3

2. Pivot element is not present:
   - Input: 6 5 4 3 2 1
   - Output: -1

3. Edge Case:
   - Input: 1 0 0 0 0
   - Output: 0


# Time Complexity and Space Complexity
```python
Time Complexity -> O(n)
(as we are traversing the list once.)
Space Complexity -> O(1)

```
<br>
<br>
<br>

<h1>PROFICIENT_TRADER</h1>
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Problem Explanation 🚀
If Input: prices = [7,1,5,3,6,4]
Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell. 

# My logic 🤯
### Approach
My approach is to find the minimun priced item in the left half and simultaneously finding the maximum profit by substracting it to the minimum price on the left. Then keep comparing to the previous maximum profit to find the final maximum profit.

<h3>Test Cases</h3>

1. Profit is possible:
   - Input: 1 2 3 4 5 6
   - Output: 5

2. Profit is not possible:
   - Input: 6 5 4 3 2 1
   - Output: 0

3. Only 1 price is given:
   - Input: 69
   - Output: 0


# Time Complexity and Space Complexity
```python
Time Complexity -> O(n)
(as we are traversing the list once.)
Space Complexity -> O(1)

```

