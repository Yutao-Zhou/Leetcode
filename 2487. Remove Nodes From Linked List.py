# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #### Recursion ###
        # if not head.next:
        #     return head
        # head.next = self.removeNodes(head.next)
        # if head.next and head.val < head.next.val:
        #     return head.next
        # return head

        #### Monotonic Stack ####
        stack = []
        cur = head
        while cur:
            while stack and cur.val > stack[-1].val:
                stack.pop()
            stack.append(cur)
            cur = cur.next

        dummy = ListNode()
        cur = dummy
        for node in stack:
            cur.next = node
            cur = cur.next
        return dummy.next