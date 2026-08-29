# [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)

## Approach

### 1st Solution: Sorting

To solve this problem, independent of the problem, we will need to have a data structure that stores the frequency of each number in the array.
To that we can use a HashMap.

Done that, the first and most simple solution would be to sort the HashMap based on the frequency values and create a list of size K that will hold the K most frequent elements.

### 2nd Solution: Heap

In most cases, when a problem asks for top K ..., the first intuition is to use a Heap.

After building the frequency map, we iterate over the unique elements and insert them into a Min Heap based on their frequency.
- We would loop through the HashMap inserting the elements into the heap, if the heap size exceeds K (capacity), we pop the first (and smallest) element.
- This way we ensure that only the top K elements are left in the heap.

In the end, we can just transform these K elements back into a list and return them.

### 3rd Solution: Counting Sort

This solution may not be obvious, but it's the most efficient.

An element can appear at most n times, where n is the length of the input array. Therefore, we can use the frequency itself as an index.

The idea is to create an array of arrays, where each subarray correspond to a specific frequency based on their index.

    [[], [], [], [], []]
     0   1   2   3   4
The indices represent the frequencies, so that all elements in the subarray 1 have a frequency of 1, all elements present in subarray 2 have a frequency of 2 and so on.

After placing every unique element into its corresponding frequency bucket, we traverse the buckets from the highest frequency to the lowest and collect elements until we have K elements.

## Complexity

Let n be the number of elements in the input array.

Sorting:
- Time Complexity: O(n log n)
- Space Complexity: O(n)

Heap:
- Time Complexity: O(n log k)
- Space Complexity: O(n)

Counting Sort:
- Time Complexity: O(n)
- Space Complexity: O(n)
