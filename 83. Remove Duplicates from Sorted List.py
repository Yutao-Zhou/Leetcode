# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #### skip #### 
        if head == None:
            return head
        ans = ListNode(0)
        ans.next = head
        while head.next:
            if head.next.val == head.val and head.next:
                head.next = head.next.next
            else:
                head = head.next
        return ans.next