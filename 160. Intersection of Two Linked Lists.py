# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #### combind ####
        A = headA
        B = headB
        while 1:
            if A == B:
                return A
            if A == None:
                A = headB
            if B == None:
                B = headA
            if A != B:
                A = A.next
                B = B.next