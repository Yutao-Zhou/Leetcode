# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #### iteritive and creat linked list ####
        # dummy = ListNode(0)
        # ans = dummy
        # cache = 0
        # while head:
        #     if head.val == 0:
        #         dummy.val = cache
        #         cache = 0
        #         if not head.next:
        #             return ans.next
        #         elif head.next:
        #             dummy.next = ListNode(0)
        #             dummy = dummy.next
        #             head = head.next
        #     else:
        #         cache += head.val
        #         head = head.next
        
        #### inplace ####
        head = head.next
        ans = head
        while head.next.next:
            if head.next.val != 0:
                head.val += head.next.val
                head.next = head.next.next
            else:
                head.next = head.next.next
                head = head.next
        head.next = None
        return ans