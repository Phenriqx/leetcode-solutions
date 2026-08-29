# [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)

## Approach

### Brute Force Solution

The brute force approach is to compare every pair of elements and check whether they are equal.

If a pair of equal elements is found, the array contains a duplicate. Otherwise, we continue checking the remaining pairs.

Since we may need to compare every element with every other element, the time complexity is O(n²).

### Optimal Solution

The key to achieve a optimal solution is to use a HashMap or a HashSet to keep track of the elements we've already seen.

While we loop through the array, we check if the current element is present in the HashSet, we know that this array contains duplicates.

If we exit the loop, it means no duplicate was found in the array.

> While a HashMap will work, a HashSet is a cleaner for this problem, since we don't need any values, we just need to know if a key exists with O(1) lookup.

## Complexity

Brute Force Solution:
- Time Complexity: O(n²)
- Space Complexity: O(1)

Optimal Solution:
- Time Complexity: O(n)
- Space Complexity: O(n)