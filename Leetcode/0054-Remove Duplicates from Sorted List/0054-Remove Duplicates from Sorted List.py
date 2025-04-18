from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        seen = set()
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            if curr.val in seen:
                prev.next = curr.next
            else:
                seen.add(curr.val)
                prev = curr
            curr = curr.next

        return dummy.next