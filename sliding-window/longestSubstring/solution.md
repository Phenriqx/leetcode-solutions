# [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

## Approach

### Brute Force Solution

A brute force approach would be to generate every possible substring and check whether each one contains duplicate characters.

We could keep track of the longest substring found that contains only unique characters.

Since there are O(n²) possible substrings and checking each substring can take O(n) time, this approach can take **O(n³)** time.

A more optimized brute-force approach could use a HashSet while generating the substrings, reducing the time complexity to **O(n²)**.

### Optimal Solution: Sliding Window

The key insight is to maintain a **sliding window** that always contains unique characters.

We use two pointers:

* `i` represents the left boundary of the window.
* `j` represents the right boundary of the window.

We also use a **HashSet** to keep track of the characters currently inside the window.

For every character at position `j`:

* If the character is not in the HashSet, we can safely add it to the current window.
* If the character is already in the HashSet, the window contains a duplicate. We then move `i` forward, removing characters from the HashSet, until the duplicate is removed.

Once the window contains only unique characters again, we calculate its length:

```text id="7k3x6n"
window length = j - i + 1
```

We keep track of the maximum window length found throughout the iteration.

For example, with:

```text id="z5v8q2"
s = "abcabcbb"
```

The window initially grows:

```text
[a]
[ab]
[abc]
```

When we encounter the second `a`, the current window would contain a duplicate. We move the left pointer forward until `a` is removed:

```text
[bc]
[bca]
```

The process continues until the entire string has been processed.

The important invariant is that **the window always contains unique characters**. This allows us to expand the window when possible and shrink it only when necessary.

## Complexity

### Brute Force

* **Time:** O(n³)
* **Space:** O(n)

With a more optimized brute-force implementation using a HashSet:

* **Time:** O(n²)
* **Space:** O(n)

### Sliding Window

* **Time:** O(n)
* **Space:** O(n)

Although the algorithm contains a nested `while` loop, the overall complexity remains O(n). Each character is added to and removed from the HashSet at most once as the two pointers move from left to right.

