# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #### two pass ####
        dummy = head
        ans = dummy
        num = []
        while head:
            num.append(head.val)
            head = head.next
        print(num)
        num[k - 1], num[-k] = num[-k], num[k - 1]
        print(num)
        i = 0
        while dummy:
            if dummy.val != num[i]:
                dummy.val = num[i]
            else:
                i += 1
                dummy = dummy.next
        return ans