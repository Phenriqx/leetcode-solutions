# [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)

## Approach

### 1st Solution: Brute Force

A straightforward solution would be to iterate through the array and, for each element, calculate the product of every other element.

For each position, we would need to traverse the entire array again, skipping the current element.

This results in **O(n²)** time complexity.

### 2nd Solution: Prefix and Suffix Products

The key observation is that the product of all elements except the current one can be divided into two parts:

```text
product of elements to the left × product of elements to the right
```

For example:

```text
Input:  [1, 2, 3, 4]

Index:   0  1  2  3

Left:   [1, 1, 2, 6]
Right:  [24,12, 4, 1]
```

For each position, multiplying its left product by its right product gives the product of every element except itself.

```text
1 × 24 = 24
1 × 12 = 12
2 × 4  = 8
6 × 1  = 6
```

So the result is:

```text
[24, 12, 8, 6]
```

We can calculate the prefix products in one pass and the suffix products in another pass.

However, we don't actually need to store both arrays.

We can store the prefix product directly in the result array. Then, while traversing the array from right to left, we maintain a running suffix product and multiply it by the prefix product already stored in the result.

This allows us to solve the problem in **O(n)** time using **O(1) extra space**, excluding the output array.

### Why We Don't Use Division

A tempting solution is to calculate the product of the entire array and divide it by each element.

However, this approach fails when the array contains zeroes and does not satisfy the intended constraints of the problem.

By using prefix and suffix products, we avoid division entirely.

## Complexity

### Brute Force

* **Time:** O(n²)
* **Space:** O(1)

### Prefix and Suffix Products

* **Time:** O(n)
* **Space:** O(1) extra space
