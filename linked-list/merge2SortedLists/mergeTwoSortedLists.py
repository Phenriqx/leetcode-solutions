from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        iter = ListNode()
        dummy = iter
        while list1 and list2:
            if list1.val <= list2.val:
                iter.next = list1
                list1 = list1.next
            else:
                iter.next = list2
                list2 = list2.next

            iter = iter.next

        if list1:
            iter.next = list1

        if list2:
            iter.next = list2

        return dummy.next