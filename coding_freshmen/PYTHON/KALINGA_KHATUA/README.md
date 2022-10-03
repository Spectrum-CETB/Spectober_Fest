# PROFICIENT_TRADER
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
