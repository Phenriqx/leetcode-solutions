# [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

## Approach

### Brute Force Solution

A brute force solution would be to consider every possible pair of days as a potential buying and selling opportunity.

For each day, we could check every future day and calculate the profit from buying on the first day and selling on the second.

We keep track of the maximum profit found.

Since we may need to compare every day with every future day, this results in **O(n²)** time complexity.

### Optimal Solution -> Sliding Window

The key observation is that, for any given selling day, the best possible profit is obtained by buying at the **lowest price seen before that day**.

We can therefore solve the problem with a single pass through the array using two pointers:

* `i` represents the day with the lowest buying price seen so far (Left Boundary).
* `j` represents the current selling day (Right boundary).

For each price:

1. If `prices[j]` is lower than `prices[i]`, we update `i` because we have found a better day to buy.
2. Otherwise, we calculate the profit from buying at `prices[i]` and selling at `prices[j]`.
3. We update the maximum profit if the current profit is higher.

This works because we only need to keep track of the **cheapest buying price seen so far**. Every time we encounter a new price, we can immediately determine the best profit we could have made by selling on that day.

The pointers always move from left to right, ensuring that the buying day always occurs before the selling day.

## Complexity

### Brute Force

* **Time:** O(n²)
* **Space:** O(1)

### Optimal

* **Time:** O(n)
* **Space:** O(1)
