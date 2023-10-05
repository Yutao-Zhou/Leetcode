# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        while head and head.next:
            node = ListNode(gcd(head.val, head.next.val))
            next_next = head.next
            head.next = node
            node.next = next_next
            head = head.next.next
        return dummy.next