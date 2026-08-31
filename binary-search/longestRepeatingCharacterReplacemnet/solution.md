# [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/description/)

## Approach

### Optimal Solution -> Sliding Window

In this problem, we want to find the longest substring containing the same letter after K replacements.

    Input: "AABABBA", k = 1
    Output: 4
    We can replace the B at index 2 to form "AAAA" or A at index 3 to form "BBBB"

For that, a good idea might be to track the most frequent characters, and replace those that differ from it until we reach K replacements.

To track the frequency of each character, we can use a HashMap with the character as the key and the frequency as the value. We also want a sliding window so we can track the current substring.

While we loop through the string, we compute the frequency of the characters:
- If the character hasn't been seen, its frequency is now 1
- If we've seen the character before, increment it by 1

We know that a window is valid if the replacements needed are less than or equal to K.

`replacements_needed = window_length - most_frequent`

If the number of replacements needed are greater than K, then window is not valid and we need to adjust the boundaries of the sliding window.
- This means that we need to update the left boundary until the window is valid.
- We do that by moving the left pointer to the right, essentially shrinking the window from the left end. While we do that, we decrease the frequency of the `s[left]` element from the map.

> We don't actually replace the elements on the string, just compute how many it'd be necessary for the window to be valid.

At every step, we update the maximum valid window length found so far.

The answer is the maximum length we found on the string.

## Complexity

### Brute Force

* **Time:** O(n²)
* **Space:** O(1)

### Optimal

* **Time:** O(n)
* **Space:** O(1)

The left and right pointers each move from left to right at most n times. Since the input contains only uppercase English letters, the frequency map contains at most 26 entries.