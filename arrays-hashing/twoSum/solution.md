# [Two Sum](https://leetcode.com/problems/two-sum/description/)

## Approach

### Brute Force Solution

A brute force solution for this problem would be to simply check every element against every other, making it a nested loop.
This solution will work, but it's far from the most optimal way to solve this problem, since its time complexity is O(n²), given the nested loops through the array.

### Optimal Solution

The optimal solution for this solution revolves around the idea of using a hashmap to store the values we have already seen along with their indices.

While we loop through the array, we compute the difference between the target and the current element:

`diff = target - current_element`

We check if this difference is in the HashMap, if so, we've found the indices the result to the target.

If the difference isn't in the hashmap, we add the current element of the array along with its index into the HashMap, because it may very well be the difference we're looking later on the array.

## Complexity

Brute Force Solution:
- Time Complexity: O(n²)
- Space Complexity: O(1)

Optimal Solution:
- Time Complexity: O(n)
- Space Complexity: O(n)