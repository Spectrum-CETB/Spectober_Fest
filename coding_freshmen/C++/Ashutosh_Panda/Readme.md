# Problem Title: Print Matrix in Spiral order

## Problem Explanation

Ex:- Given Matrix :
                    1  2  3
                    4  5  6
                    7  8  9
Output- 1 2 3 6 9 8 7 4 5

## Logic and Intuition

* An optimized approach will be to create 4 variables that store the upper ,lower ,left and right bound of the Matrix which decreases after each iteration.
* We will iterate through every row and column in a spiral manner until the lower and right bound are greater than upper and left bound respectively.

## Time Complexity and Space Complexity

* Time Complexity: O(m*n)
* Space Complexity: O(1)


# Problem Title: Sieve of Eratosthenes

To find all the prime numbers upto a given number.

## Logic & Intuition

* We will create a bool array which is used to check if a number is prime or not (initially all are set to true).
* We will iterate the array $\sqrt{n}$ times and in each iteration we will mark all the multiples of i as false.
* At the end of the loop the remaining array will contain only the prime numbers.

## Time Complexity and Space Complexity

* Time Complexity: O(n * log(log(n)) )
* Space Complexity: O(n)
