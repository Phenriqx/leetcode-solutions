# [Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

## Approach

### 1st Solution: Sorting

A straightforward solution is to sort both strings and compare the resulting strings.

If two strings are anagrams, they contain exactly the same characters with the same frequencies. Therefore, after sorting, their characters will appear in the same order.

For example:

```text id="e9gk2w"
"anagram" → "aaagmnr"
"nagaram" → "aaagmnr"
```

Since the sorted strings are equal, they are anagrams.

### 2nd Solution: Character Frequency

A more efficient approach is to count the frequency of each character in both strings.

We can use a **HashMap** to store the frequency of each character in the first string and then decrement the frequency as we iterate through the second string.

If a character does not exist in the map, or its frequency becomes invalid, the strings cannot be anagrams.

Alternatively, since the problem only contains lowercase English letters, we can use an array of size 26 instead of a HashMap.

For each character in the first string, we increment its corresponding position in the array. For each character in the second string, we decrement it.

If the strings are anagrams, every frequency will eventually return to zero.

## Complexity

### Sorting

* **Time:** O(n log n)
* **Space:** O(n)

### Character Frequency

* **Time:** O(n)
* **Space:** O(1)

The frequency-based solution uses O(1) extra space because the frequency array always contains exactly 26 positions, regardless of the input size. Alternately, a hashMap would use O(n) extra space.
