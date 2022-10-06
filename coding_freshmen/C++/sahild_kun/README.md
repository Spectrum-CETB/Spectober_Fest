# 1.MAJORITY__ELEMENT
We are given an array of size n and we have to return a Majority element .
# Problem Explanation 🚀

here we have to return the Majority element that is the  array element that ocurrs more than n/2 times

# Your logic 🤯
* first i took the array input then traversed thru the array and on every same array element upadted a variable count ....if the count exceeds n/2 that means 
it satisifies the given question criteria and then as sonn as the criterion is met i print out the number and stop other executions using break
* [3,2,3]  [1,2,2,2,5]
* libraray used :- <iostream> c++ library

# Time Complexity and Space Complexity
cpp


 Time Complexity -> O(n^2)
 Space Complexity -> O(n)
 
# 2.PROFICENT_TRADER

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Problem Explanation 🚀

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
So what we have to is basically find the profits and from them return the maximum profit ...if the profit are not there return  0;

# Your logic 🤯
* first i input the stock prices that is a array where i represents the day .
*now we compare the prices of ith day and its next days till n..if price increases we calculate the diff
*now if the diff is greater than earlier profit then profit updates and maximum profit is printed and if no profit then 0 is printed
*test cases -[1,2,3,4], [7,1,5,3,6,4]

# Time Complexity and Space Complexity
cpp


 Time Complexity -> O(n^2)
 Space Complexity -> O(n)
 
