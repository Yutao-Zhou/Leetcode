# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #### recursive swap ####
        # if not head or not head.next:
        #     return head
        # second = head.next
        # head.next = self.swapPairs(second.next)
        # second.next = head
        # return second
        
        #### interitive ####
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            cur.next = second
            first.next = second.next
            second.next = first
            cur = cur.next.next
        return dummy.next