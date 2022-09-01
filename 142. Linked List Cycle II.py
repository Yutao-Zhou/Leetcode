# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #### Slow Fast Pointers ####
        slow, fast = head, head
        seen = set()
        while 1:
            if not fast or not fast.next:
                return None
            if fast.next in seen:
                return fast.next
            if fast.next.next in seen:
                return fast.next.next
            else:
                seen.add(slow)
                fast = fast.next.next
                slow = slow.next