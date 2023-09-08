# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #### Recursion ####
        # if not head: return None
        # head.next = self.removeElements(head.next, val)
        # if head.val == val:
        #     return head.next
        # return head

        #### Iterative ####
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur and cur.next:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
        return dummy.next