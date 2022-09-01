# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #### Split and Rebuild ####
        smaller, larger = ListNode(-200), ListNode(-200)
        s, l = smaller, larger
        while head:
            if head.val < x:
                smaller.next = ListNode(head.val)
                smaller = smaller.next
            else:
                larger.next = ListNode(head.val)
                larger = larger.next
            head = head.next
        smaller.next = l.next
        return s.next