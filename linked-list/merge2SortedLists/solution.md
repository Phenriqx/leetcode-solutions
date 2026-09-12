# [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

## Solution

For this problem, we need to return a new sorted list made up from two other sorted lists.

So, in order to do that, we need to create a new node that will point to this new list, along with a dummy node that will only point to the head of the result list.

We loop while both lists are valid
- At each iteration we compare the values of the current nodes of each list
- If, let's say, the value of the current node of list 1 is smaller than the value of the current node of list 2, we set next pointer of the result list to point to this node, and then we move the head of list 1 to the next element
- At the end of the iteration, we move the result node to the next (which is the value we just assigned)

At the end of the loop, it means that either we have our complete result list or one list ended before the other (maybe one list has all the values smaller than the other, so it would be traversed first).
- In the latter case, we can just assign the result's next pointer to the rest of the list that was not fully traversed.

In the end, we just return the head of this new list

## Complexity

* **Time:** O(n + m)
    - Where `n` is the length of list1 and `m` is the length of list2.
* **Space:** O(1)
