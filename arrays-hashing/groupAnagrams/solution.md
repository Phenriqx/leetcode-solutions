# [Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)

## Approach

### 1st Solution: Sorting

A straightforward way to identify anagrams is to sort the characters of each string.

Two strings are anagrams if, after sorting their characters, they produce the same string.

For example:

```text
"eat" → "aet"
"tea" → "aet"
"ate" → "aet"
```

Since all three strings produce the same sorted representation, they belong to the same group.

We can use a **HashMap** where the sorted string acts as the key and the values are the strings that share that key.

After processing all strings, the values stored in the HashMap are the groups of anagrams.

### 2nd Solution: Character Frequency

Instead of sorting every string, we can use the **frequency of each character** as the key.

Since the problem uses lowercase English letters, we can create an array of size 26 to count how many times each character appears.

For example:

```text
"eat"

a → 1
e → 1
t → 1

Frequency:
[1, 0, 0, 0, 1, ..., 1, ...]
```

Two strings are anagrams if they contain exactly the same characters with exactly the same frequencies.

Therefore, strings with identical frequency arrays can be placed in the same group.

We use the frequency representation as the key in a HashMap:

```text
frequency → list of anagrams
```

For every string:

1. Create a frequency array of size 26.
2. Count the occurrences of each character.
3. Use the frequency array as the HashMap key.
4. Add the string to the corresponding group.

At the end, the values of the HashMap contain all the groups of anagrams.

## Complexity

Let `n` be the number of strings and `k` be the maximum length of a string.

### Sorting

* **Time:** O(n · k log k)
* **Space:** O(n · k)

### Character Frequency

* **Time:** O(n · k)
* **Space:** O(n · k)

The frequency-based approach avoids sorting each string and is therefore more efficient when the strings are large.
