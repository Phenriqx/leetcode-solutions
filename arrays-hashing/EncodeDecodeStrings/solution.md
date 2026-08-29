# [Encode and Decode Strings](https://neetcode.io/problems/string-encode-and-decode/question)

## Approach

In this problem, we need to decode a list of strings in a deterministic way, so that the decoding function always reaches the same list of strings.

The first thought may be to join the strings using a delimiter, like a comma, but we'd quickly run into a problem, for instance:

    Input: ["Hello,World", "User"]
    Encode -> "Hello,World,User"
    Decode -> ["Hello", "World", "User"]

If the strings themselves contain the delimiter, our decode function will split them based on the delimiter, causing the result to have more strings than expected.

A solid approach is to use length of each string along with a symbol as the delimiters.

To encode, we loop through the list of strings, and for each string, we prepend it with its length and a symbol (like @ or #), and then append this new string to our result string.

To decode, we use the same method. Since every word comes with its length and a delimiter, we know exactly how many characters to read and when a word begins or ends. So, using the same example from above:

    Input: ["Hello,World", "User"]
    Encode -> "11@Hello,World4@User"
    Decode -> ["Hello,World", "User"]


## Complexity

Let n be the total number of characters across all input strings.

Encode:
- Time Complexity: O(n)
- Space Complexity: O(n)

Decode:
- Time Complexity: O(n)
- Space Complexity: O(n)