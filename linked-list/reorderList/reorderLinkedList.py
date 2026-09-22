# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        prev = slow.next = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        left, right = head, prev
        while left and right:
            l_next, r_next = left.next, right.next
            left.next = right
            right.next = l_next

            # move pointers
            right = r_next
            left = l_next