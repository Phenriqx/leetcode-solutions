# [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## Solution

Reversing a Linked List is all about pointer manipulation.
We traverse the linked list from left to right, re-assigning the next pointer of the current node to point to the node behind it.

To avoid losing track of the rest of the list we need 3 pointers:
- `curr`: the current node we're processing
- `prev`: the node that should come after `curr` once reversed
- `next`: the original next node of the current node, so we don't lose track.

We initially set `curr` to point to our current head and `prev` to a null node.

We then loop while `curr` is not null, meaning that there are nodes still left to process.
- `next` will point to the next node of current
- Having saved the next pointer, we can re-assign the current next pointer to point to the previous node (initially null)
- Set the previous node to point to our current node
- Move forward with the current node, moving it to the `next` node.

The reversed list is saved at `prev`, which is the new head of the list.

## Complexity

* **Time:** O(n)
* **Space:** O(1)
