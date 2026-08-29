# [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)

## Approach

### Brute Force Solution

A brute force approach is to consider every element in the array as the potential beginning of a consecutive sequence.

For each element, we repeatedly check whether the next number exists and count how long the sequence is.

In the worst case, we may traverse the same sequence multiple times, resulting in O(n²) time complexity.

### Optimal Solution

To solve this problem efficiently, we first need a few things:

1. Remove duplicates from array
2. O(1) lookup if an element is present in the array
3. Determine whether a number is the beginning of a consecutive sequence

First, to remove any duplicate values from the input array, what we can do is just transform the array into a HashSet, this will remove any duplicates and also give us O(1) lookup of an element.

Second, we need to know if the current number we're on is a sequence.
We can know this be checking if the number has a predecessor (current number - 1), this is where the HashSet comes in handy, giving us O(1) lookup.

- If the element has a predecessor, it means the element is part of a sequence, but is not the first element of that sequence, so we can just skip it.
- If the element doesn't have a predecessor, it means it may be the first element of a sequence.
    - In this case, we check if the element has a successor, while the successor exists, we increment the count of the current sequence.

By only starting a sequence when its first element is found, we avoid repeatedly traversing the same sequence.

In the end, we return the longest consecutive sequence we found.

## Complexity

Brute Force Solution:
- Time Complexity: O(n²)
- Space Complexity: O(1) or O(n) depending on the solution.

Optimal Solution:
- Time Complexity: O(n)
- Space Complexity: O(n)