class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy

        
        for _ in range(n):
            if fast.next:
                fast = fast.next
            else:
                return head

        
        while fast.next:
            slow = slow.next
            fast = fast.next

        
        slow.next = slow.next.next

        return dummy.next