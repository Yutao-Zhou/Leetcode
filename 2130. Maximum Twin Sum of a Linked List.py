# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #### Stack and two pointers ####
        maxTwin = 0
        stack = []
        i = head
        j = head
        while i:
            if j:
                stack.append(i.val)
                j = j.next.next
            else:
                twinSum = stack.pop() + i.val
                if twinSum > maxTwin:
                    maxTwin = twinSum
            i = i.next
        return maxTwin