# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #### Run first ####
        # l, r = head, head
        # # let it run first so they would be n node away
        # while n > 0:
        #     r = r.next
        #     n -= 1
        # if not r:
        #     return head.next
        # # riched target distance run together
        # while r.next:
        #     r = r.next
        #     l = l.next
        # l.next = l.next.next
        # return head
        
        #### Dummy for better code ####
        dummy = ListNode
        dummy.next = head
        l, r = dummy, dummy
        # let it run first so they would be n node away
        while n > 0:
            r = r.next
            n -= 1
        # riched target distance run together
        while r.next:
            r = r.next
            l = l.next
        l.next = l.next.next
        return dummy.next