# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #### add one by one ####
        ans = ListNode(0)
        dummy = ans
        last = 0
        while l1 or l2:
            cache = 0
            if l1 :
                cache += l1.val
                l1 = l1.next
            if l2:
                cache += l2.val
                l2 = l2.next
            cache += last
            ans.val = cache % 10
            if l1 or l2:
                ans.next = ListNode(0)
                ans = ans.next
            last = cache // 10
        if last != 0:
            ans.next = ListNode(last)
        return dummy