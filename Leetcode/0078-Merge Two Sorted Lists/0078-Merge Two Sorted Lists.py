# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        l, r = list1, list2
        
        while l and r:
            if l.val < r.val:
                current.next = l
                l = l.next
            else:
                current.next = r
                r = r.next
            current = current.next
        
        
        current.next = l if l else r
        
        return dummy.next
